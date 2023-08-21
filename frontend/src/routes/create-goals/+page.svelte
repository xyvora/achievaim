<script lang="ts">
  import { onMount } from 'svelte';
  import type { PageData } from './$types';
  import { goto } from '$app/navigation';
  import type { DaysOfWeekInput, GoalCreate, GoalInfo, GoalSuggestionCreate } from '$lib/generated';
  import DaysOfWeekSelector from '$lib/components/DaysOfWeekSelector.svelte';
  import Message from '$lib/components/Message.svelte';
  import { createGoal, createOpenAiSuggestion } from '$lib/api';
  import { goals, setToast } from '$lib/stores/stores';

  export let data: PageData;

  onMount(() => {
    if (!data.isAuthenticated) {
      goto('/');
    }
  });

  let goal: GoalCreate = {
    days_of_week: {
      monday: false,
      tuesday: false,
      wednesday: false,
      thursday: false,
      friday: false,
      saturday: false,
      sunday: false,
    },
  };

  let selectAll = false;
  let goalError = false;
  let specificLocked = false;
  let measurableLocked = false;
  let achievableLocked = false;
  let relevantLocked = false;
  let timeBoundLocked = false;

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
      const response = await createGoal(goal);
      goals.set(response);
      setToast('Goal successfully saved.');
      goto('/');
    } catch (error) {
      console.log(error);
    }
  }

  let loadingGenerate = false;

  async function handleGenerate() {
    loadingGenerate = true;
    goalError = false;

    if (!goal.goal) {
      goalError = true;
      return;
    }

    let goalSuggestionCreate: GoalSuggestionCreate = { goal: goal.goal };

    if (goal.specific) {
      const specific: GoalInfo = { info: goal.specific, locked: specificLocked };
      goalSuggestionCreate.specific = specific;
    }
    if (goal.measurable) {
      const measurable: GoalInfo = { info: goal.measurable, locked: measurableLocked };
      goalSuggestionCreate.measurable = measurable;
    }
    if (goal.achievable) {
      const achievable: GoalInfo = { info: goal.achievable, locked: achievableLocked };
      goalSuggestionCreate.achievable = achievable;
    }
    if (goal.relevant) {
      const relevant: GoalInfo = { info: goal.relevant, locked: relevantLocked };
      goalSuggestionCreate.relevant = relevant;
    }
    if (goal.time_bound) {
      const timeBound: GoalInfo = { info: goal.time_bound, locked: timeBoundLocked };
      goalSuggestionCreate.time_bound = timeBound;
    }

    try {
      const suggestion = await createOpenAiSuggestion(goalSuggestionCreate);
      goal.goal = suggestion.goal;
      goal.specific = suggestion.specific;
      goal.measurable = suggestion.measurable;
      goal.achievable = suggestion.achievable;
      goal.relevant = suggestion.relevant;
      goal.time_bound = suggestion.time_bound;
    } catch (error) {
      console.log(error);
    }

    loadingGenerate = false;
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
      <Message
        messageId="goal-error"
        message="SMART goal is required"
        showMessage={goalError}
        isError={true}
      />

      <div class="flex flex-col mt-3 items-left">
        <button id="generate" class="btn rounded-xl btn-primary" on:click={handleGenerate}
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
          <input type="checkbox" class="toggle toggle-primary" bind:checked={specificLocked} />
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
          <input type="checkbox" class="toggle toggle-primary" bind:checked={measurableLocked} />
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

    <!-- achievable card -->
    <div class="flex flex-col w-full p-4 card card-body">
      <h2 class="mb-2 card-title">Achievable</h2>
      <div class="flex flex-col w-full md:flex-row">
        <input
          id="achievable"
          class="flex-grow w-full px-3 py-2 mb-2 leading-tight border shadow appearance-none rounded-xl focus:outline-none focus:shadow-outline md:mb-0"
          type="text"
          placeholder="AchievAIm's Achievable suggestion. e.g. Find enjoyable activities."
          bind:value={goal.achievable}
        />
        <label
          class="flex items-center justify-end w-full mt-2 cursor-pointer label md:ml-2 md:mt-0 md:w-auto"
        >
          <input type="checkbox" class="toggle toggle-primary" bind:checked={achievableLocked} />
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
          <input type="checkbox" class="toggle toggle-primary" bind:checked={relevantLocked} />
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
          <input type="checkbox" class="toggle toggle-primary" bind:checked={timeBoundLocked} />
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
        <button class="btn rounded-xl btn-primary" id="save-goal-button" on:click={handleSave}
          >Save Smart Goal</button
        >
      </div>
    </div>

    <div class="flex">
      <div class="divider" />
    </div>
  </div>
</div>
