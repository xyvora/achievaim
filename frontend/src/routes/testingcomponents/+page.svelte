<script lang="ts">
  type DaysOfWeek = {
    monday: boolean;
    tuesday: boolean;
    wednesday: boolean;
    thursday: boolean;
    friday: boolean;
    saturday: boolean;
    sunday: boolean;
  };

  type Goal = {
    days_of_week: DaysOfWeek;
    date_for_achievement?: string;
    time_of_day?: string;
  };

  let goal: Goal = {
    days_of_week: {
      monday: false,
      tuesday: false,
      wednesday: false,
      thursday: false,
      friday: false,
      saturday: false,
      sunday: false
    }
  };

  import DaysOfWeekSelector from '$lib/components/DaysOfWeekSelector.svelte';
  import { page } from '$app/stores';
</script>

<div class="page-fade-in">
  <div class="container shadow-lg rounded-xl mb-4 mx-auto px-4 pt-5 md:max-w-xl lg:max-w-3xl z-10">
    <div class="mb-5">
      <div class="card w-full">
        <figure>
          <figcaption class="p-4 card-body flex flex-col">
            <div class="flex items-center mb-2">
              <a
                href="/edit-goal"
                aria-label="edit-goal"
                title="Edit Goal"
                class="{$page.url.pathname === '/edit-goal'
                  ? 'rounded bg-white'
                  : ''} block text-xl font-bold mr-2"
              >
                Goal
              </a>
              <div class="flex items-center">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  class="w-4 h-4 stroke-current text-info mr-1"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M10.5 19.5L3 12m0 0l7.5-7.5M3 12h18"
                  />
                </svg>
                <span class="text-xs text-gray-500 italic">Click Goal to edit</span>
              </div>
            </div>
            <div
              class="border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
            >
              What's your SMART Goal?
            </div>
          </figcaption>
        </figure>
      </div>
    </div>

    <!-- Specific card -->
    <div class="card w-full">
      <figure>
        <figcaption class="p-4 card-body flex flex-col">
          <h2 class="card-title mb-2">Specific</h2>
          <div class="flex flex-col md:flex-row w-full">
            <div
              class="border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
            >
              AchievAIm's Specific suggestion
            </div>
          </div>
        </figcaption>
      </figure>
    </div>

    <!-- Measurable card -->
    <div class="card w-full">
      <figure>
        <figcaption class="p-4 card-body flex flex-col">
          <h2 class="card-title mb-2">Measurable</h2>
          <div class="flex flex-col md:flex-row w-full">
            <div
              class="border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
            >
              AchievAIm's Measurable suggestion
            </div>
          </div>
        </figcaption>
      </figure>
    </div>

    <!-- Attainable card -->
    <div class="card w-full">
      <figure>
        <figcaption class="p-4 card-body flex flex-col">
          <h2 class="card-title mb-2">Attainable</h2>
          <div class="flex flex-col md:flex-row w-full">
            <div
              class="border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
            >
              AchievAIm's Attainable suggestion
            </div>
          </div>
        </figcaption>
      </figure>
    </div>

    <!-- Relevant card -->
    <div class="card w-full">
      <figure>
        <figcaption class="p-4 card-body flex flex-col">
          <h2 class="card-title mb-2">Relevant</h2>
          <div class="flex flex-col md:flex-row w-full">
            <div
              class="border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
            >
              AchievAIm's Relevant suggestion
            </div>
          </div>
        </figcaption>
      </figure>
    </div>

    <!-- Time-Bound card -->
    <div class="card w-full">
      <figure>
        <figcaption class="p-4 card-body flex flex-col">
          <h2 class="card-title mb-2">Time-Bound</h2>
          <div class="flex flex-col md:flex-row w-full">
            <div
              class="border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
            >
              AchievAIm's Time-Bound suggestion
            </div>
          </div>
        </figcaption>
      </figure>
    </div>

    <div class="mt-3 flex flex-col items-center">
      <div class="card w-full">
        <figure>
          <figcaption class="p-4 card-body flex flex-col items-center">
            {#if goal.days_of_week}
              <div class="flex justify-between items-center w-full">
                <h2 class="card-title mb-2">Days</h2>
              </div>
              <DaysOfWeekSelector daysOfWeek={goal.days_of_week} />
            {/if}
          </figcaption>
        </figure>
      </div>
    </div>

    <div class="card w-full">
      <figure>
        <figcaption class="p-4 card-body flex flex-row items-center">
          <h2 class="card-title mb-2">Date</h2>
          <div class="flex-grow flex items-center relative">
            <input
              class="shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
              id="goal-date"
              type="date"
              bind:value={goal.date_for_achievement}
              aria-describedby="date-description"
              readonly
            />
          </div>
        </figcaption>
      </figure>
    </div>

    <div class="card w-full">
      <figure>
        <figcaption class="p-4 card-body flex flex-row items-center">
          <h2 class="card-title mb-2">Time</h2>
          <div class="flex-grow flex items-center">
            <input
              class="shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
              id="goal-time"
              type="time"
              bind:value={goal.time_of_day}
              aria-describedby="time-description"
              readonly
            />
          </div>
        </figcaption>
      </figure>
    </div>
  </div>
</div>

<style>
  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }

  .page-fade-in {
    animation: fadeIn 1s ease-in-out;
  }
</style>
