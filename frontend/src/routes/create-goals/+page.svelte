<script lang="ts">
  import { onMount, createEventDispatcher } from 'svelte';
  import type { DaysOfWeek, GoalCreate } from '$lib/generated';

  let daysOfWeek: DaysOfWeek = {
    monday: false,
    tuesday: false,
    wednesday: false,
    thrusday: false,
    friday: false,
    saturday: false,
    sunday: false
  };

  let selectAll = false;

  const toggleAll = () => {
    selectAll = !selectAll;
    daysOfWeek = daysOfWeek.map((day) => ({ ...day, selected: selectAll }));
  };

  let goalDate: string;
  let goalTime: string;

  const dispatch = createEventDispatcher();

  function handleClick() {
    dispatch('save');
    // add your saving logic here
  }

  let loadingGenerate = false;
  let loadingSave = false;

  const handleClickGenerate = async () => {
    loadingGenerate = true;
    // Simulate an API call delay
    await new Promise((resolve) => setTimeout(resolve, 2000));
    loadingGenerate = false;
  };

  const handleClickSave = async () => {
    loadingSave = true;
    // Simulate an API call delay
    await new Promise((resolve) => setTimeout(resolve, 2000));
    loadingSave = false;
  };
</script>

<div class="flex">
  <div class="divider" />
</div>
<div class="container mx-auto px-4 pt-5 md:max-w-xl lg:max-w-3xl z-10">
  <div class="mb-5">
    <label class="block text-xl font-bold mb-2" for="goal"> Goal </label>
    <input
      class="shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
      id="goal"
      type="text"
      placeholder="What's your SMART Goal?"
    />

    <div class="mt-3 flex flex-col items-left">
      <button
        id="generate"
        class="btn btn-primary"
        on:click={handleClickGenerate}
        disabled={loadingGenerate}
      >
        Generate
      </button>
      {#if loadingGenerate}
        <div class="mt-3 flex justify-center items-center">
          <span class="loading loading-infinity loading-md" />
        </div>
      {/if}
    </div>
    <div class="mt-3 flex flex-col items-right">
      <button id="save" class="btn btn-primary" on:click={handleClickSave} disabled={loadingSave}>
        Save
      </button>
      {#if loadingSave}
        <div class="mt-3 flex justify-center items-center">
          <span class="loading loading-infinity loading-md" />
        </div>
      {/if}
    </div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
    <!-- Specific card -->
    <div class="card bordered">
      <figure>
        <figcaption class="p-4 card-body">
          <h2 class="card-title">Specific</h2>
          <p id="specific" class="text-gray-600" contenteditable="true">
            SmartGoalAI's Specific suggestion
          </p>
          <div class="mt-3">
            <button on:click={handleClick} class="btn btn-primary">Keep Specific Suggestion</button>
          </div>
        </figcaption>
      </figure>
    </div>

    <!-- Measurable card -->
    <div class="card bordered">
      <figure>
        <figcaption class="p-4 card-body">
          <h2 class="card-title">Measurable</h2>
          <p id="measurable" class="text-gray-600" contenteditable="true">
            SmartGoalAI's Measurable suggestion
          </p>
          <div class="mt-3">
            <button on:click={handleClick} class="btn btn-primary"
              >Keep Measurable Suggestion</button
            >
          </div>
        </figcaption>
      </figure>
    </div>

    <!-- Attainable card -->
    <div class="card bordered">
      <figure>
        <figcaption class="p-4 card-body">
          <h2 class="card-title">Attainable</h2>
          <p id="attainable" class="text-gray-600" contenteditable="true">
            SmartGoalAI's Attainable suggestion
          </p>
          <div class="mt-3">
            <button on:click={handleClick} class="btn btn-primary"
              >Keep Attainable Suggestion</button
            >
          </div>
        </figcaption>
      </figure>
    </div>

    <!-- Relevant card -->
    <div class="card bordered">
      <figure>
        <figcaption class="p-4 card-body">
          <h2 class="card-title">Relevant</h2>
          <p id="relevant" class="text-gray-600" contenteditable="true">
            SmartGoalAI's Relevant suggestion
          </p>
          <div class="mt-3">
            <button on:click={handleClick} class="btn btn-primary">Keep Relevant Suggestion</button>
          </div>
        </figcaption>
      </figure>
    </div>

    <!-- Time-Bound card -->
    <div class="card bordered">
      <figure>
        <figcaption class="p-4 card-body">
          <h2 class="card-title">Time-Bound</h2>
          <p id="time-bound" class="text-gray-600" contenteditable="true">
            SmartGoalAI's Time-Bound suggestion
          </p>
          <div class="mt-3">
            <button on:click={handleClick} class="btn btn-primary"
              >Keep Time-Bound Suggestion</button
            >
          </div>
        </figcaption>
      </figure>
    </div>
  </div>
</div>

<div class="mt-4 pd-4 flex flex-col items-center">
  <span class="block text-xl font-bold mb-2">Select the Days Your SMART Goal Repeats:</span>
  <button class="btn btn-primary mt-4" on:click={toggleAll}>
    {#if selectAll}Deselect All{:else}Select All{/if}
  </button>
  <div class="grid grid-cols-2 md:grid-cols- gap-5 mt-4">
    {#each daysOfWeek as day (day.name)}
      <div class="rounded shadow p-2">
        <label class="inline-flex items-center">
          <input
            type="checkbox"
            class={day.selected ? 'toggle toggle-primary' : 'toggle toggle-info'}
            bind:checked={day.selected}
          />
          <span class="ml-2 text-md">{day.name}</span>
        </label>
      </div>
    {/each}
  </div>
</div>

<div class="mt-4 flex flex-col items-center">
  <label class="block text-lg font-bold mb-2" for="goal-date">
    Choose the Date for Completing Your SMART Goal. Usually Associated with Bigger Goals:
  </label>
  <input
    bind:value={goalDate}
    class="shadow appearance-none border rounded w-1/2 py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
    id="goal-date"
    type="date"
  />
  <label class="block text-lg font-bold mb-2 mt-4" for="goal-time">
    Choose the Time for Your SMART Goal Alert:
  </label>
  <input
    bind:value={goalTime}
    class="shadow appearance-none border rounded w-1/2 py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
    id="goal-time"
    type="time"
  />
</div>

<div class="mt-4 flex flex-col items-center">
  <button class="btn btn-primary" on:click={handleClick}>Save Smart Goal</button>
</div>

<div class="flex">
  <div class="divider" />
</div>
