<script lang="ts">
  import type { GoalOutput } from '$lib/generated';
  import DaysOfWeekSelector from '$lib/components/DaysOfWeekSelector.svelte';

  export let goal: GoalOutput;
</script>

<div
  class="collapse md:ml-3 mb-3 bg-primary text-primary-content focus:bg-secondary focus:text-secondary-content"
>
  <div class="collapse-title">
    <div
      class="container shadow-lg rounded-xl mb-4 mx-auto px-4 pt-5 md:max-w-xl lg:max-w-3xl z-10"
    >
      <div class="mb-5">
        <div class="card w-full">
          <figure>
            <figcaption class="p-4 card-body flex flex-col">
              <div class="flex items-center mb-2">
                <a href="/edit-goal/{goal.id}" aria-label="edit-goal" title="Edit Goal"> Goal </a>
                <div class="dropdown dropdown-right">
                  <button class="btn btn-circle btn-ghost btn-xs text-info">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 24 24"
                      class="w-4 h-4 stroke-white"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                      />
                    </svg>
                  </button>
                  <button
                    class="card compact text-left text-primary dropdown-content z-[1] shadow bg-base-100 rounded-box w-64"
                  >
                    <div class="card-body">
                      <p>Click the Goal Text to the left to edit your SMART goal.</p>
                    </div>
                  </button>
                </div>
              </div>
              <div
                class="border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
              >
                {goal.goal}
              </div>
            </figcaption>
          </figure>
        </div>
      </div>
    </div>
  </div>
  <div class="collapse-content">
    <div
      class="container shadow-lg rounded-xl mb-4 mx-auto px-4 pt-5 md:max-w-xl lg:max-w-3xl z-10"
    >
      <!-- Rest of the Content goes here -->
      <!-- Specific card -->
      <div class="card w-full">
        <figure>
          <figcaption class="p-4 card-body flex flex-col">
            <h2 class="card-title mb-2">Specific</h2>
            <div class="flex flex-col md:flex-row w-full">
              <div
                class="border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
              >
                {#if goal.specific}
                  {goal.specific}
                {:else}
                  Not set
                {/if}
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
                {#if goal.measurable}
                  {goal.measurable}
                {:else}
                  Not set
                {/if}
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
                {#if goal.attainable}
                  {goal.attainable}
                {:else}
                  Not set
                {/if}
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
                {#if goal.relevant}
                  {goal.relevant}
                {:else}
                  Not set
                {/if}
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
                {#if goal.time_bound}
                  {goal.time_bound}
                {:else}
                  Not set
                {/if}
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
                class="shadow text-secondary appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
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
                class="shadow text-secondary appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
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
</div>
