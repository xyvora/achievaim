<script lang="ts">
  // import { onMount } from 'svelte';
  import { createGoal } from '$lib/api';
  // import { Goal } from '$lib/generated/models/Goal';

  let goal = '';
  // let goals: Goal[];
  let suggestions = [];

  const handleSubmit = async () => {
    if (goal) {
      await createGoal(goal);
      goal = '';
      // goals = await getGoals();
    }
  };

  /* onMount(async () => {
    goals = await getGoals();
  }); */

  const handleGenerateSuggestions = async () => {
    if (goal) {
      suggestions = await generateSuggestions(goal);
    }
  };

  const selectSuggestion = (suggestion) => {
    goal = suggestion;
  };
</script>

<head>
  <title>Create Your Goals</title>
</head>
<div clas="overflow-x-auto">
  <form class="mb-4" on:submit={handleSubmit}>
    <input
      type="text"
      class="px-2 py-1 border border-gray-300 rounded"
      bind:value={goal}
      placeholder="Enter your SMART goal"
    />
    <button
      type="submit"
      class="px-4 py-2 ml-2 font-bold text-white bg-blue-500 rounded hover:bg-blue-600"
      >Create Goal</button
    >
  </form>

  <button
    on:click={handleGenerateSuggestions}
    class="px-4 py-2 font-bold text-white bg-green-500 rounded hover:bg-green-600"
    >Generate Suggestions</button
  >

  <div>
    <h3 class="mt-4 text-lg font-semibold">Suggestions:</h3>
    {#each suggestions as suggestion}
      <div class="px-4 py-2 my-2 border border-gray-300 rounded">
        <p>{suggestion}</p>
        <button
          on:click={() => selectSuggestion(suggestion)}
          class="px-4 py-2 mt-2 font-semibold text-white bg-blue-500 rounded hover:bg-blue-600"
          >Select</button
        >
      </div>
    {/each}
  </div>
</div>

<style>
  input[type='text'] {
    width: 300px;
  }
</style>
