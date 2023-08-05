<script lang="ts">
  import type { DaysOfWeek, GoalCreate } from '$lib/generated';
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
        goal.days_of_week![day as keyof DaysOfWeek] = selectAll;
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
</script>

<div class="page-fade-in">
  <div class="container z-10 px-4 pt-5 mx-auto mb-4 shadow-lg rounded-xl md:max-w-xl lg:max-w-3xl">
    <div class="w-full card">
      <div class="flex items-center mb-5">
        <!-- Flex container for alignment -->
        <label class="block mb-2 text-xl font-bold rounded-xl" for="goal">Goal</label>
        <div class="dropdown dropdown-right">
          <button tabindex="0" class="m-3 btn btn-circle btn-ghost btn-xs text-info">
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
            <div class="text-left normal-case card-body text-primary">
              <p>Enter your SMART goal and any details e.g. Exercise to get healthier</p>
              <p>Click Generate to have AchievAIm suggest the SMART details</p>
              <p>Toggle Right to Lock on the details you like →</p>
              <p>
                ← Toggle Left to Unlock and press Generate again to give you another suggestion for
                that specific SMART detail
              </p>
            </div>
          </div>
        </div>
      </div>
      <!-- Flex container ends here -->
      <input
        class="w-full px-3 py-2 leading-tight border shadow appearance-none rounded-xl focus:outline-none focus:shadow-outline"
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

      <div class="flex flex-col mt-3 items-left">
        <button id="generate" class="btn rounded-xl btn-primary" on:click={handleClick}
          >Generate</button
        >
        {#if loadingGenerate}
          <div class="flex items-center justify-center mt-3">
            <span class="loading loading-infinity loading-md" />
          </div>
        {/if}
      </div>
    </div>
    <!-- Specific card -->
    <div class="flex flex-col w-full p-4 card card-body">
      <h2 class="mb-2 card-title">Specific</h2>
      <div class="flex flex-col w-full md:flex-row">
        <input
          id="specific"
          class="flex-grow w-full px-3 py-2 mb-2 leading-tight border shadow appearance-none rounded-xl focus:outline-none focus:shadow-outline md:mb-0"
          type="text"
          placeholder="AchievAIm's Specific suggestion. e.g. 15 min daily exercise."
          bind:value={goal.specific}
        />
        <label
          class="flex items-center justify-end w-full mt-2 cursor-pointer label md:ml-2 md:mt-0 md:w-auto"
        >
          <input type="checkbox" class="toggle toggle-primary" />
          <div class="dropdown dropdown-end">
            <button tabindex="0" class="m-3 btn btn-circle btn-ghost btn-xs text-info">
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
                <div class="text-left card-body text-primary normal-case">
                  <p>← Toggle Left to unlock</p>
                  <div class="text-right text-primary normal-case">
                    <p>Toggle Right to Lock →</p>
                  </div>
                </div>
              </div></button
            >
          </div>
        </label>
      </div>
    </div>

    <!-- Measurable card -->
    <div class="flex flex-col w-full p-4 card card-body">
      <h2 class="mb-2 card-title">Measurable</h2>
      <div class="flex flex-col w-full md:flex-row">
        <input
          id="measurable"
          class="flex-grow w-full px-3 py-2 mb-2 leading-tight border shadow appearance-none rounded-xl focus:outline-none focus:shadow-outline md:mb-0"
          type="text"
          placeholder="AchievAIm's Measurable suggestion. e.q. Track consecutive days."
          bind:value={goal.measurable}
        />
        <label
          class="flex items-center justify-end w-full mt-2 cursor-pointer label md:ml-2 md:mt-0 md:w-auto"
        >
          <input type="checkbox" class="toggle toggle-primary" />
          <div class="dropdown dropdown-end">
            <button tabindex="0" class="m-3 btn btn-circle btn-ghost btn-xs text-info">
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
                <div class="text-left card-body text-primary normal-case">
                  <p>← Toggle Left to unlock</p>
                  <div class="text-right text-primary normal-case">
                    <p>Toggle Right to Lock →</p>
                  </div>
                </div>
              </div></button
            >
          </div>
        </label>
      </div>
    </div>

    <!-- Attainable card -->
    <div class="flex flex-col w-full p-4 card card-body">
      <h2 class="mb-2 card-title">Attainable</h2>
      <div class="flex flex-col w-full md:flex-row">
        <input
          id="attainable"
          class="flex-grow w-full px-3 py-2 mb-2 leading-tight border shadow appearance-none rounded-xl focus:outline-none focus:shadow-outline md:mb-0"
          type="text"
          placeholder="AchievAIm's Attainable suggestion. e.g. Find enjoyable activities."
          bind:value={goal.attainable}
        />
        <label
          class="flex items-center justify-end w-full mt-2 cursor-pointer label md:ml-2 md:mt-0 md:w-auto"
        >
          <input type="checkbox" class="toggle toggle-primary" />
          <div class="dropdown dropdown-end">
            <button tabindex="0" class="m-3 btn btn-circle btn-ghost btn-xs text-info">
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
                <div class="text-left card-body text-primary normal-case">
                  <p>← Toggle Left to unlock</p>
                  <div class="text-right text-primary normal-case">
                    <p>Toggle Right to Lock →</p>
                  </div>
                </div>
              </div></button
            >
          </div>
        </label>
      </div>
    </div>

    <!-- Relevant card -->
    <div class="flex flex-col w-full p-4 card card-body">
      <h2 class="mb-2 card-title">Relevant</h2>
      <div class="flex flex-col w-full md:flex-row">
        <input
          id="relevant"
          class="flex-grow w-full px-3 py-2 mb-2 leading-tight border shadow appearance-none rounded-xl focus:outline-none focus:shadow-outline md:mb-0"
          type="text"
          placeholder="AchievAIm's Relevant suggestion. e.g. Improve fitness."
          bind:value={goal.relevant}
        />
        <label
          class="flex items-center justify-end w-full mt-2 cursor-pointer label md:ml-2 md:mt-0 md:w-auto"
        >
          <input type="checkbox" class="toggle toggle-primary" />
          <div class="dropdown dropdown-end">
            <button tabindex="0" class="m-3 btn btn-circle btn-ghost btn-xs text-info">
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
                <div class="text-left card-body text-primary normal-case">
                  <p>← Toggle Left to unlock</p>
                  <div class="text-right text-primary normal-case">
                    <p>Toggle Right to Lock →</p>
                  </div>
                </div>
              </div></button
            >
          </div>
        </label>
      </div>
    </div>

    <!-- Time-Bound card -->
    <div class="flex flex-col w-full p-4 card card-body">
      <h2 class="mb-2 card-title">Time-Bound</h2>
      <div class="flex flex-col w-full md:flex-row">
        <input
          id="time-bound"
          class="flex-grow w-full px-3 py-2 mb-2 leading-tight border shadow appearance-none rounded-xl focus:outline-none focus:shadow-outline md:mb-0"
          type="text"
          placeholder="AchievAIm's Time-Bound suggestion. e.g. 30 consecutive days."
          bind:value={goal.time_bound}
        />
        <label
          class="flex items-center justify-end w-full mt-2 cursor-pointer label md:ml-2 md:mt-0 md:w-auto"
        >
          <input type="checkbox" class="toggle toggle-primary" />
          <div class="dropdown dropdown-end">
            <button tabindex="0" class="m-3 btn btn-circle btn-ghost btn-xs text-info">
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
                <div class="text-left card-body text-primary normal-case">
                  <p>← Toggle Left to unlock</p>
                  <div class="text-right text-primary normal-case">
                    <p>Toggle Right to Lock →</p>
                  </div>
                </div>
              </div></button
            >
          </div>
        </label>
      </div>
    </div>

    <div class="flex flex-col items-center mt-3">
      <div class="w-full card">
        <figure>
          <figcaption class="flex flex-col items-center p-4 card-body">
            {#if goal.days_of_week}
              <div class="flex items-center justify-between w-full">
                <h2 class="mb-2 card-title">Days</h2>

                <div class="flex items-center">
                  <label for="selectAll" class="flex items-center cursor-pointer label">
                    <input
                      type="checkbox"
                      class="toggle toggle-primary"
                      id="selectAll"
                      bind:checked={selectAll}
                      on:click={toggleAll}
                    />
                    <label
                      class="flex items-center justify-end w-full mt-2 cursor-pointer label md:ml-2 md:mt-0 md:w-auto"
                    >
                      <div class="dropdown dropdown-end">
                        <button tabindex="0" class="m-3 btn btn-circle btn-ghost btn-xs text-info">
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
                          <div
                            class="card compact dropdown-content z-[1] bg-base-100 rounded-box w-64"
                          >
                            <div class="text-left card-body text-primary normal-case">
                              <p>These are the days of the week your goals repeat</p>
                              <div class="text-right text-primary normal-case">
                                <p>Toggle right to select all →</p>
                              </div>
                            </div>
                          </div>
                        </button>
                      </div>
                    </label>
                  </label>
                </div>
              </div>
              <DaysOfWeekSelector daysOfWeek={goal.days_of_week} />
            {/if}
          </figcaption>
        </figure>
      </div>
    </div>
    <div class="flex flex-col items-center mt-3">
      <div class="w-full card">
        <figure>
          <figcaption class="flex flex-row items-center p-4 card-body">
            <h2 class="mb-2 card-title">Time</h2>
            <div class="flex items-center flex-grow">
              <input
                class="w-full px-3 py-2 leading-tight border shadow appearance-none rounded-xl focus:outline-none focus:shadow-outline"
                id="goal-time"
                type="time"
                bind:value={goal.time_of_day}
                aria-describedby="time-description"
              />
              <div class="justify-end w-full mt-2 dropdown dropdown-end md:ml-2 md:mt-0 md:w-auto">
                <!-- Replaced label tag with div -->
                <button tabindex="0" class="m-3 btn btn-circle btn-ghost btn-xs text-info">
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
                    <div class="text-left card-body text-primary normal-case">
                      <p>Set the alert time for your SMART goals for selected days above.</p>
                    </div>
                  </div>
                </button>
              </div>
            </div>
          </figcaption>
        </figure>
      </div>

      <div class="w-full card">
        <figure>
          <figcaption class="flex flex-row items-center p-4 card-body">
            <h2 class="mb-2 card-title">Date</h2>
            <div class="relative flex items-center flex-grow">
              <input
                class="w-full px-3 py-2 leading-tight border shadow appearance-none rounded-xl focus:outline-none focus:shadow-outline"
                id="goal-date"
                type="date"
                bind:value={goal.date_for_achievement}
                aria-describedby="date-description"
              />
              <div class="justify-end w-full mt-2 dropdown dropdown-end md:ml-2 md:mt-0 md:w-auto">
                <!-- Replaced label tag with div -->
                <button tabindex="0" class="m-3 btn btn-circle btn-ghost btn-xs text-info">
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
                    <div class="text-left card-body text-primary normal-case">
                      <p>Choose the Date for Completing Your SMART Goal.</p>
                    </div>
                  </div>
                </button>
              </div>
            </div>
          </figcaption>
        </figure>
      </div>
      <div class="flex flex-col mt-3 items-left">
        <button class="btn rounded-xl btn-primary" on:click={handleSave}>Save Smart Goal</button>
      </div>
    </div>

    <div class="flex">
      <div class="divider" />
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
