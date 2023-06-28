<script lang="ts">
  import type { PageData } from './$types';
  import { createGoal, getGoals } from '$lib/api';
  import { RepeatsEvery } from '$lib/generated';
  import type { GoalBase } from '$lib/generated';

  export let data: PageData;

  let goal = '';
  let suggestions: string[] = [];

  const handleCreateGoal = async () => {
    let goalObj: GoalBase = {
      name: goal,
      duration: 0,
      daysOfWeek: {
        monday: false,
        tuesday: false,
        wednesday: false,
        thursday: false,
        friday: false,
        saturday: false,
        sunday: false
      },
      repeatsEvery: RepeatsEvery.DAY,
      progress: 0
    };
    await createGoal(goalObj);
    goal = '';
    data.goals = await getGoals();
  };

  const handleGenerateSuggestions = async () => {
    console.log('Handled');
    /* if (goal) {
      suggestions = await generateSuggestions(goal);
    } */
  };

  const selectSuggestion = (suggestion: string) => {
    goal = suggestion;
  };
</script>

<head>
  <title>Create Your Goals</title>
</head>
<div class="overflow-x-auto">
  <form class="mb-4" on:submit={handleCreateGoal}>
    <input
      type="text"
      class="px-2 py-1 border border-gray-300 rounded"
      bind:value={goal}
      placeholder="Enter your SMART goal"
    />
    <button type="submit" id="btnCreateGoal" class="btn btn-primary">Create Goal</button>
  </form>

  <button on:click={handleGenerateSuggestions} id="btnGenerateSuggestions" class="btn btn-secondary"
    >Generate Suggestions</button
  >

  <div>
    <h3 class="mt-4 text-lg font-semibold">Suggestions:</h3>
    {#each suggestions as suggestion}
      <div class="px-4 py-2 my-2 border border-gray-300 rounded">
        <p>{suggestion}</p>
        <button on:click={() => selectSuggestion(suggestion)} class="btn btn-secondary"
          >Select</button
        >
      </div>
    {/each}
  </div>

  <div>
    <h3 class="mt-4 text-lg font-semibold">Current Goals:</h3>
    {#if data.goals && data.goals.length > 0}
      {#each data.goals as goal}
        <div>
          <ul>
            <li>{goal.name}</li>
          </ul>
        </div>
      {/each}
    {:else}
      <div>No goals found</div>
    {/if}
  </div>
</div>

<style>
  input[type='text'] {
    width: 300px;
  }
</style>
