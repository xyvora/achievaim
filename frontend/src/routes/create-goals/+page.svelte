<script lang="ts">
  import DaysOfWeekSelector from '$lib/components/DaysOfWeekSelector.svelte';
  import type { DaysOfWeek } from '$lib/generated';

  let daysOfWeek: DaysOfWeek = {
    monday: false,
    tuesday: false,
    wednesday: false,
    thursday: false,
    friday: false,
    saturday: false,
    sunday: false
  };

  let selectAll = false;

  const toggleAll = () => {
    selectAll = !selectAll;
    Object.keys(daysOfWeek).forEach((day) => {
      daysOfWeek[day as keyof DaysOfWeek] = selectAll;
    });
  };

  let goalDate: string;
  let goalTime: string;

  let loadingGenerate = false;
</script>

<div class="flex">
  <div class="divider" />
</div>
<div class="container mx-auto px-4 pt-5 md:max-w-xl lg:max-w-3xl z-10">
  <div class="mb-5">
    <label class="block text-xl font-bold mb-2" for="goal">Goal</label>
    <input
      class="shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
      id="goal"
      type="text"
      placeholder="What's your SMART Goal?"
    />

    <div class="mt-3 flex flex-col items-left">
      <button id="generate" class="btn btn-primary">Generate</button>
      {#if loadingGenerate}
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
          <input
            id="specific"
            class="shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
            type="text"
            placeholder="AchievAIm's Specific suggestion"
          />
          <div class="mt-3">
            <button class="btn btn-primary">Keep Specific Suggestion</button>
          </div>
        </figcaption>
      </figure>
    </div>

    <!-- Measurable card -->
    <div class="card bordered">
      <figure>
        <figcaption class="p-4 card-body">
          <h2 class="card-title">Measurable</h2>
          <input
            id="measurable"
            class="shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
            type="text"
            placeholder="AchievAIm's Measurable suggestion"
          />
          <div class="mt-3">
            <button class="btn btn-primary">Keep Measurable Suggestion</button>
          </div>
        </figcaption>
      </figure>
    </div>

    <!-- Attainable card -->
    <div class="card bordered">
      <figure>
        <figcaption class="p-4 card-body">
          <h2 class="card-title">Attainable</h2>
          <input
            id="attainable"
            class="shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
            type="text"
            placeholder="AchievAIm's Attainable suggestion"
          />
          <div class="mt-3">
            <button class="btn btn-primary">Keep Attainable Suggestion</button>
          </div>
        </figcaption>
      </figure>
    </div>

    <!-- Relevant card -->
    <div class="card bordered">
      <figure>
        <figcaption class="p-4 card-body">
          <h2 class="card-title">Relevant</h2>
          <input
            id="relevant"
            class="shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
            type="text"
            placeholder="AchievAIm's Relevant suggestion"
          />
          <div class="mt-3">
            <button class="btn btn-primary">Keep Relevant Suggestion</button>
          </div>
        </figcaption>
      </figure>
    </div>

    <!-- Time-Bound card -->
    <div class="card bordered">
      <figure>
        <figcaption class="p-4 card-body">
          <h2 class="card-title">Time-Bound</h2>
          <input
            id="time-bound"
            class="shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
            type="text"
            placeholder="AchievAIm's Time-Bound suggestion"
          />
          <div class="mt-3">
            <button class="btn btn-primary">Keep Time-Bound Suggestion</button>
          </div>
        </figcaption>
      </figure>
    </div>
  </div>
</div>

<div class="mt-4 p-4 flex flex-col items-center">
  <span class="block text-xl font-bold mb-2">Days Your SMART Goal Repeats:</span>
  <DaysOfWeekSelector {daysOfWeek} />
</div>

<div class="mt-4 flex flex-col items-center">
  <div class="text-center w-300px mb-2">
    <label class="block text-lg" for="goal-time">
      Set the Alert Time for Your SMART Goals
    </label>
    <p class="text-sm text-gray-600 text-left">
      on Selected Days
    </p>
  </div>
  <input
    bind:value={goalTime}
    class="shadow appearance-none border rounded w-300px py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
    id="goal-time"
    type="time"
  />
</div>

<div class="mt-4 flex flex-col items-center">
  <div class="text-center w-300px mb-2">
    <label class="block text-lg" for="goal-date">
      Choose the Date for Your SMART Goal
    </label>
    <p class="text-sm text-gray-600 text-left">
      Usually Associated with Bigger Goals
    </p>
  </div>
  <input
    bind:value={goalDate}
    class="shadow appearance-none border rounded w-300px py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
    id="goal-date"
    type="date"
  />
</div>

<div class="mt-4 flex flex-col items-center">
  <button class="btn btn-primary">Save Smart Goal</button>
</div>

<div class="flex">
  <div class="divider" />
</div>
