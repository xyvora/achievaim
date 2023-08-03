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
  let loadingGenerate = false;
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

  let showModal = false; // Modal state

  const openModal = () => {
    showModal = true;
  };

  const closeModal = () => {
    showModal = false;
  };

  const handleEdit = () => {
    // Handle the edit logic here...
    closeModal();
  };
</script>

<div class="page-fade-in">
  <div class="divider" />

  <div class="container shadow-lg rounded-xl mb-4 mx-auto px-4 pt-5 md:max-w-xl lg:max-w-3xl z-10">
    <div class="mb-5">
      <label class="block text-xl font-bold mb-2" for="goal">Goal</label>
      <input
        class="shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
        id="goal"
        type="text"
        placeholder="What's your SMART Goal?"
        bind:value={goal.goal}
      />
      <ErrorMessage
        errorMessageId="goal-error"
        errorMessage="SMART goal is required"
        showError={goalError}
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

    <!-- Specific card -->
    <div class="card w-full">
      <figure>
        <figcaption class="p-4 card-body flex flex-col">
          <h2 class="card-title mb-2">Specific</h2>
          <div class="flex flex-col md:flex-row w-full">
            <input
              id="specific"
              class="shadow appearance-none border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
              type="text"
              placeholder="AchievAIm's Specific suggestion"
              bind:value={goal.specific}
            />
            <label
              class="cursor-pointer label flex items-center md:ml-2 mt-2 md:mt-0 w-full md:w-auto justify-end"
            >
              <input type="checkbox" class="toggle toggle-primary" checked />
              <div class="dropdown dropdown-end">
                <button tabindex="0" class="btn btn-circle btn-ghost btn-xs text-info m-3">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    class="w-4 h-4 stroke-current"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                    />
                  </svg>
                  <button class="card compact dropdown-content z-[1] bg-base-100 rounded-box w-64">
                    <div class="card-body">
                      <h2 class="card-title">You needed more info?</h2>
                      <p>Here is a description!</p>
                    </div>
                  </button>
                </button>
              </div>
            </label>
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
            <input
              id="measurable"
              class="shadow appearance-none border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
              type="text"
              placeholder="AchievAIm's Measurable suggestion"
              bind:value={goal.measurable}
            />
            <label
              class="cursor-pointer label flex items-center md:ml-2 mt-2 md:mt-0 w-full md:w-auto justify-end"
            >
              <input type="checkbox" class="toggle toggle-primary" checked />
              <div class="dropdown dropdown-end">
                <button tabindex="0" class="btn btn-circle btn-ghost btn-xs text-info m-3">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    class="w-4 h-4 stroke-current"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                    />
                  </svg>
                  <button class="card compact dropdown-content z-[1] bg-base-100 rounded-box w-64">
                    <div class="card-body">
                      <h2 class="card-title">You needed more info?</h2>
                      <p>Here is a description!</p>
                    </div>
                  </button>
                </button>
              </div>
            </label>
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
            <input
              id="attainable"
              class="shadow appearance-none border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
              type="text"
              placeholder="AchievAIm's Attainable suggestion"
              bind:value={goal.attainable}
            />
            <label
              class="cursor-pointer label flex items-center md:ml-2 mt-2 md:mt-0 w-full md:w-auto justify-end"
            >
              <input type="checkbox" class="toggle toggle-primary" checked />
              <div class="dropdown dropdown-end">
                <button tabindex="0" class="btn btn-circle btn-ghost btn-xs text-info m-3">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    class="w-4 h-4 stroke-current"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                    />
                  </svg>
                  <button class="card compact dropdown-content z-[1] bg-base-100 rounded-box w-64">
                    <div class="card-body">
                      <h2 class="card-title">You needed more info?</h2>
                      <p>Here is a description!</p>
                    </div>
                  </button>
                </button>
              </div>
            </label>
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
            <input
              id="relevant"
              class="shadow appearance-none border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
              type="text"
              placeholder="AchievAIm's Relevant suggestion"
              bind:value={goal.relevant}
            />
            <label
              class="cursor-pointer label flex items-center md:ml-2 mt-2 md:mt-0 w-full md:w-auto justify-end"
            >
              <input type="checkbox" class="toggle toggle-primary" checked />
              <div class="dropdown dropdown-end">
                <button tabindex="0" class="btn btn-circle btn-ghost btn-xs text-info m-3">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    class="w-4 h-4 stroke-current"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                    />
                  </svg>
                  <button class="card compact dropdown-content z-[1] bg-base-100 rounded-box w-64">
                    <div class="card-body">
                      <h2 class="card-title">You needed more info?</h2>
                      <p>Here is a description!</p>
                    </div>
                  </button>
                </button>
              </div>
            </label>
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
            <input
              id="time-bound"
              class="shadow appearance-none border rounded-xl w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline flex-grow mb-2 md:mb-0"
              type="text"
              placeholder="AchievAIm's Time-Bound suggestion"
              bind:value={goal.time_bound}
            />
            <label
              class="cursor-pointer label flex items-center md:ml-2 mt-2 md:mt-0 w-full md:w-auto justify-end"
            >
              <input type="checkbox" class="toggle toggle-primary" checked />
              <div class="dropdown dropdown-end">
                <button tabindex="0" class="btn btn-circle btn-ghost btn-xs text-info m-3">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    class="w-4 h-4 stroke-current"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                    />
                  </svg>
                  <button class="card compact dropdown-content z-[1] bg-base-100 rounded-box w-64">
                    <div class="card-body">
                      <h2 class="card-title">You needed more info?</h2>
                      <p>Here is a description!</p>
                    </div>
                  </button>
                </button>
              </div>
            </label>
          </div>
        </figcaption>
      </figure>
    </div>

    <div class="mt-3 flex flex-col items-center">
      <div class="card">
        <figure>
          <figcaption class="p-4 card-body flex flex-col items-center">
            {#if goal.days_of_week}
              <div class="flex justify-between items-center w-full">
                <span class="block text-xl font-bold"> Days </span>
                <div class="flex items-center">
                  <label for="selectAll" class="cursor-pointer label flex items-center">
                    <input
                      type="checkbox"
                      class="toggle toggle-primary"
                      id="selectAll"
                      bind:checked={selectAll}
                      on:click={toggleAll}
                    />
                  </label>
                  <div class="dropdown dropdown-end">
                    <button tabindex="-1" class="btn btn-circle btn-ghost btn-xs text-info m-3">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        class="w-4 h-4 stroke-current"
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
                      <div class="card-body">
                        <h2 class="card-title">You needed more info?</h2>
                        <p>Here is a description!</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <DaysOfWeekSelector daysOfWeek={goal.days_of_week} />
            {/if}
          </figcaption>
        </figure>
      </div>
    </div>

    <div class="card">
      <figure>
        <figcaption class="p-4 card-body flex flex-row items-center">
          <label class="text-left text-lg font-bold mb-2" for="goal-time">Time:</label>
          <div class="flex-grow flex items-center">
            <input
              class="shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
              id="goal-time"
              type="time"
              bind:value={goal.time_of_day}
              aria-describedby="time-description"
            />
            <label
              class="cursor-pointer label flex items-center md:ml-2 mt-2 md:mt-0 w-full md:w-auto justify-end"
            >
              <input type="checkbox" class="toggle toggle-primary" checked />
              <div class="dropdown dropdown-end">
                <button tabindex="0" class="btn btn-circle btn-ghost btn-xs text-info m-3">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    class="w-4 h-4 stroke-current"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                    />
                  </svg>
                  <button class="card compact dropdown-content z-[1] bg-base-100 rounded-box w-64">
                    <div class="card-body">
                      <h2 class="card-title">You needed more info?</h2>
                      <p>Here is a description!</p>
                    </div>
                  </button>
                </button>
              </div>
            </label>
          </div>
        </figcaption>
      </figure>
    </div>

    <div class="card">
      <figure>
        <figcaption class="p-4 card-body flex flex-row items-center">
          <label class="text-left text-lg font-bold mb-2" for="goal-date">Date:</label>
          <div class="flex-grow flex items-center relative">
            <input
              class="shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
              id="goal-date"
              type="date"
              bind:value={goal.date_for_achievement}
              aria-describedby="date-description"
            />
            <label
              class="cursor-pointer label flex items-center md:ml-2 mt-2 md:mt-0 w-full md:w-auto justify-end"
            >
              <input type="checkbox" class="toggle toggle-primary" checked />
              <div class="dropdown dropdown-end">
                <button tabindex="0" class="btn btn-circle btn-ghost btn-xs text-info m-3">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    class="w-4 h-4 stroke-current"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                    />
                  </svg>
                  <button class="card compact dropdown-content z-[1] bg-base-100 rounded-box w-64">
                    <div class="card-body">
                      <h2 class="card-title">You needed more info?</h2>
                      <p>Here is a description!</p>
                    </div>
                  </button>
                </button>
              </div>
            </label>
          </div>
        </figcaption>
      </figure>
    </div>
  </div>
</div>

<div class="flex">
  <div class="divider" />
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
