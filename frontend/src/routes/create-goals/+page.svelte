<script lang="ts">
  import type { DaysOfWeekInput, GoalCreate } from '$lib/generated';
  import DaysOfWeekSelector from '$lib/components/DaysOfWeekSelector.svelte';
  import ErrorMessage from '$lib/components/ErrorMessage.svelte';
  import { createGoal } from '$lib/api';

  let goal: GoalCreate = {
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

  let selectAll = false;

  let goalError = false;

  const toggleAll = () => {
    selectAll = !selectAll;
    if (goal.days_of_week) {
      Object.keys(goal.days_of_week).forEach((day) => {
        // goal.days_of_week! is because TypeScript sucks and won't believe days_of_week is not
        // undefined even when it is checked first.
        // eslint-disable-next-line @typescript-eslint/no-non-null-assertion
        goal.days_of_week![day as keyof DaysOfWeekInput] = selectAll;
      });
    }
  };

  async function handleSave() {
    goalError = false;

    if (!goal.goal) {
      goalError = true;
    }

    if (goalError) {
      return;
    }

    try {
      await createGoal(goal);
    } catch (error) {
      console.log(error);
    }
  }

  let loadingGenerate = false;

  function handleClick() {
    loadingGenerate = true;

    // Simulate an async operation
    setTimeout(() => {
      loadingGenerate = false;
    }, 2000);
  }

  import { blur } from 'svelte/transition';
  let isOpen = false;

  function toggleDropdown() {
    isOpen = !isOpen;
  }
</script>

<div class="page-fade-in">
  <div class="container shadow-lg rounded-xl mb-4 mx-auto px-4 pt-5 md:max-w-xl lg:max-w-3xl z-10">
    <div class="card w-full">
      <div class="mb-5 flex items-center">
        <!-- Flex container for alignment -->
        <label class="block text-xl rounded-xl font-bold mb-2" for="goal">Goal</label>
        <div class="dropdown dropdown-right">
          <button tabindex="0" class="btn btn-circle btn-ghost btn-xs text-info m-3">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              class="w-4 h-4 stroke-primary"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
          </button>
          <div class="card compact dropdown-content z-[1] bg-base-100 rounded-box w-64">
            <!-- Removed button tag wrapping div -->
            <div class="card-body text-primary text-left">
              <p>Toggle left to unsave.</p>
              <p>Generate Button above to give you another suggestion.</p>
              <p>Toggle Right to Save.</p>
            </div>
          </div>
        </div>
      </div>
      <!-- Flex container ends here -->
      <input
        class="shadow appearance-none border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
        id="goal"
        type="text"
        placeholder="What's your SMART Goal? e.g. Exercise"
        bind:value={goal.goal}
      />
      <ErrorMessage
        errorMessageId="goal-error"
        errorMessage="SMART goal is required"
        showError={goalError}
      />

      <div class="mt-3 flex flex-col items-left">
        <button id="generate" class="btn btn-primary" on:click={handleClick}>Generate</button>
        {#if loadingGenerate}
          <div class="mt-3 flex justify-center items-center">
            <span class="loading loading-infinity loading-md" />
          </div>
        {/if}
      </div>
    </div>

    <!-- Specific card -->
    <div class="card w-full p-4 card-body flex flex-col">
      <h2 class="card-title mb-2">Specific</h2>
      <div class="flex flex-col md:flex-row w-full">
        <input
          id="specific"
          class="shadow appearance-none border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
          type="text"
          placeholder="AchievAIm's Specific suggestion. e.g. 15 min daily exercise."
          bind:value={goal.specific}
        />
        <label
          class="cursor-pointer label flex items-center md:ml-2 mt-2 md:mt-0 w-full md:w-auto justify-end"
        >
          <input type="checkbox" class="toggle toggle-primary" />
          <div class="dropdown dropdown-end">
            <button
              tabindex="0"
              class="btn btn-circle btn-ghost btn-xs text-info m-3"
              on:click={toggleDropdown}
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                class="w-4 h-4 stroke-primary"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                />
              </svg>
              {#if isOpen}
                <div
                  transition:blur
                  class="card compact dropdown-content z-[1] bg-base-100 rounded-box w-64 absolute"
                >
                  <div class="card-body text-primary text-left">
                    <p>Toggle left to unsave.</p>
                    <p>Generate Button above to give you another suggestion.</p>
                    <p>Toggle Right to Save.</p>
                  </div>
                </div>
              {/if}
            </button>
          </div>
        </label>
      </div>
    </div>

    <!-- Measurable card -->
    <div class="card w-full p-4 card-body flex flex-col">
      <h2 class="card-title mb-2">Measurable</h2>
      <div class="flex flex-col md:flex-row w-full">
        <input
          id="measurable"
          class="shadow appearance-none border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
          type="text"
          placeholder="AchievAIm's Measurable suggestion. e.q. Track consecutive days."
          bind:value={goal.measurable}
        />
        <label
          class="cursor-pointer label flex items-center md:ml-2 mt-2 md:mt-0 w-full md:w-auto justify-end"
        >
          <input type="checkbox" class="toggle toggle-primary" />
          <div class="dropdown dropdown-end">
            <button tabindex="0" class="btn btn-circle btn-ghost btn-xs text-info m-3">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                class="w-4 h-4 stroke-primary"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                />
              </svg>
              <button class="card compact dropdown-content z-[1] bg-base-100 rounded-box w-64">
                <div class="card-body text-primary text-left">
                  <p>Toggle left to unsave.</p>
                  <p>Generate Button above to give you another suggestion.</p>
                  <p>Toggle Right to Save.</p>
                </div>
              </button>
            </button>
          </div>
        </label>
      </div>

      <!-- Attainable card -->
      <div class="card w-full p-4 card-body flex flex-col">
        <h2 class="card-title mb-2">Attainable</h2>
        <div class="flex flex-col md:flex-row w-full">
          <input
            id="attainable"
            class="shadow appearance-none border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
            type="text"
            placeholder="AchievAIm's Attainable suggestion. e.g. Find enjoyable activities."
            bind:value={goal.attainable}
          />
          <label
            class="cursor-pointer label flex items-center md:ml-2 mt-2 md:mt-0 w-full md:w-auto justify-end"
          >
            <input type="checkbox" class="toggle toggle-primary" />
            <div class="dropdown dropdown-end">
              <button tabindex="0" class="btn btn-circle btn-ghost btn-xs text-info m-3">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  class="w-4 h-4 stroke-primary"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                  />
                </svg>
                <button class="card compact dropdown-content z-[1] bg-base-100 rounded-box w-64">
                  <div class="card-body text-primary text-left">
                    <p>Toggle left to unsave.</p>
                    <p>Generate Button above to give you another suggestion.</p>
                    <p>Toggle Right to Save.</p>
                  </div>
                </button>
              </button>
            </div>
          </label>
        </div>
      </div>

      <!-- Relevant card -->
      <div class="card w-full p-4 card-body flex flex-col">
        <h2 class="card-title mb-2">Relevant</h2>
        <div class="flex flex-col md:flex-row w-full">
          <input
            id="relevant"
            class="shadow appearance-none border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
            type="text"
            placeholder="AchievAIm's Relevant suggestion. e.g. Improve fitness."
            bind:value={goal.relevant}
          />
          <label
            class="cursor-pointer label flex items-center md:ml-2 mt-2 md:mt-0 w-full md:w-auto justify-end"
          >
            <input type="checkbox" class="toggle toggle-primary" />
            <div class="dropdown dropdown-end">
              <button tabindex="0" class="btn btn-circle btn-ghost btn-xs text-info m-3">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  class="w-4 h-4 stroke-primary"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                  />
                </svg>
                <button class="card compact dropdown-content z-[1] bg-base-100 rounded-box w-64">
                  <div class="card-body text-primary text-left">
                    <p>Toggle left to unsave.</p>
                    <p>Generate Button above to give you another suggestion.</p>
                    <p>Toggle Right to Save.</p>
                  </div>
                </button>
              </button>
            </div>
          </label>
        </div>
      </div>

      <!-- Time-Bound card -->
      <div class="card w-full p-4 card-body flex flex-col">
        <h2 class="card-title mb-2">Time-Bound</h2>
        <div class="flex flex-col md:flex-row w-full">
          <input
            id="time-bound"
            class="shadow appearance-none border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
            type="text"
            placeholder="AchievAIm's Time-Bound suggestion. e.g. 30 consecutive days."
            bind:value={goal.time_bound}
          />
          <label
            class="cursor-pointer label flex items-center md:ml-2 mt-2 md:mt-0 w-full md:w-auto justify-end"
          >
            <input type="checkbox" class="toggle toggle-primary" />
            <div class="dropdown dropdown-end">
              <button tabindex="0" class="btn btn-circle btn-ghost btn-xs text-info m-3">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  class="w-4 h-4 stroke-primary"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                  />
                </svg>
                <button class="card compact dropdown-content z-[1] bg-base-100 rounded-box w-64">
                  <div class="card-body text-primary text-left">
                    <p>Toggle left to unsave.</p>
                    <p>Generate Button above to give you another suggestion.</p>
                    <p>Toggle Right to Save.</p>
                  </div>
                </button>
              </button>
            </div>
          </label>
        </div>
      </div>

      <div class="mt-3 flex flex-col items-center">
        <div class="card w-full">
          <figure>
            <figcaption class="p-4 card-body flex flex-col items-center">
              {#if goal.days_of_week}
                <div class="flex justify-between items-center w-full">
                  <h2 class="card-title mb-2">Days</h2>

                  <div class="flex items-center">
                    <label for="selectAll" class="cursor-pointer label flex items-center">
                      <input
                        type="checkbox"
                        class="toggle toggle-primary"
                        id="selectAll"
                        bind:checked={selectAll}
                        on:click={toggleAll}
                      />
                      <label
                        class="cursor-pointer label flex items-center md:ml-2 mt-2 md:mt-0 w-full md:w-auto justify-end"
                      >
                        <div class="dropdown dropdown-end">
                          <button
                            tabindex="0"
                            class="btn btn-circle btn-ghost btn-xs text-info m-3"
                          >
                            <svg
                              xmlns="http://www.w3.org/2000/svg"
                              fill="none"
                              viewBox="0 0 24 24"
                              class="w-4 h-4 stroke-primary"
                            >
                              <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="2"
                                d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                              />
                            </svg>
                            <button
                              class="card compact dropdown-content z-[1] bg-base-100 rounded-box w-64"
                            >
                              <div class="card-body text-primary text-left">
                                <p>These are the days of the week your goals repeat</p>
                                <p>Toggle right to select all</p>
                              </div>
                            </button></button
                          >
                        </div>
                      </label></label
                    >
                  </div>
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
            <h2 class="card-title mb-2">Time</h2>
            <div class="flex-grow flex items-center">
              <input
                class="shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
                id="goal-time"
                type="time"
                bind:value={goal.time_of_day}
                aria-describedby="time-description"
              />
              <div class="dropdown dropdown-end md:ml-2 mt-2 md:mt-0 w-full md:w-auto justify-end">
                <!-- Replaced label tag with div -->
                <button tabindex="0" class="btn btn-circle btn-ghost btn-xs text-info m-3">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    class="w-4 h-4 stroke-primary"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                    />
                  </svg>
                  <div class="card compact dropdown-content z-[1] bg-base-100 rounded-box w-64">
                    <!-- Removed button tag wrapping div -->
                    <div class="card-body text-primary text-left">
                      <p>Set the alert time for your SMART goals for selected days above.</p>
                    </div>
                  </div>
                </button>
              </div>
            </div>
          </figcaption>
        </figure>
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
              />
              <div class="dropdown dropdown-end md:ml-2 mt-2 md:mt-0 w-full md:w-auto justify-end">
                <!-- Replaced label tag with div -->
                <button tabindex="0" class="btn btn-circle btn-ghost btn-xs text-info m-3">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    class="w-4 h-4 stroke-primary"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                    />
                  </svg>
                  <div class="card compact dropdown-content z-[1] bg-base-100 rounded-box w-64">
                    <!-- Removed button tag wrapping div -->
                    <div class="card-body text-primary text-left">
                      <p>Choose the Date for Completing Your SMART Goal.</p>
                    </div>
                  </div>
                </button>
              </div>
            </div>
          </figcaption>
        </figure>
      </div>
      <div class="mt-3 flex flex-col items-left">
        <button class="btn btn-primary" on:click={handleSave}>Save Smart Goal</button>
      </div>
    </div>
  </div>
  <div class="flex">
    <div class="divider" />
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
