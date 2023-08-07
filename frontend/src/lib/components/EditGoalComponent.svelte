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
      sunday: false,
    },
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

    <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
      <!-- Specific card -->
      <div class="card">
        <figure>
          <figcaption class="p-4 card-body">
            <h2 class="card-title">Specific</h2>
            <input
              id="specific"
              class="shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
              type="text"
              placeholder="AchievAIm's Specific suggestion"
              bind:value={goal.specific}
            />
            <div class="mt-3">
              <button class="btn btn-primary">Keep Specific Suggestion</button>
            </div>
          </figcaption>
        </figure>
      </div>

      <!-- Measurable card -->
      <div class="card">
        <figure>
          <figcaption class="p-4 card-body">
            <h2 class="card-title">Measurable</h2>
            <input
              id="measurable"
              class="shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
              type="text"
              placeholder="AchievAIm's Measurable suggestion"
              bind:value={goal.measurable}
            />
            <div class="mt-3">
              <button class="btn btn-primary">Keep Measurable Suggestion</button>
            </div>
          </figcaption>
        </figure>
      </div>

      <!-- Attainable card -->
      <div class="card">
        <figure>
          <figcaption class="p-4 card-body">
            <h2 class="card-title">Attainable</h2>
            <input
              id="attainable"
              class="shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
              type="text"
              placeholder="AchievAIm's Attainable suggestion"
              bind:value={goal.attainable}
            />
            <div class="mt-3">
              <button class="btn btn-primary">Keep Attainable Suggestion</button>
            </div>
          </figcaption>
        </figure>
      </div>

      <!-- Relevant card -->
      <div class="card">
        <figure>
          <figcaption class="p-4 card-body">
            <h2 class="card-title">Relevant</h2>
            <input
              id="relevant"
              class="shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
              type="text"
              placeholder="AchievAIm's Relevant suggestion"
              bind:value={goal.relevant}
            />
            <div class="mt-3">
              <button class="btn btn-primary">Keep Relevant Suggestion</button>
            </div>
          </figcaption>
        </figure>
      </div>

      <!-- Time-Bound card -->
      <div class="card">
        <figure>
          <figcaption class="p-4 card-body">
            <h2 class="card-title">Time-Bound</h2>
            <input
              id="time-bound"
              class="shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
              type="text"
              placeholder="AchievAIm's Time-Bound suggestion"
              bind:value={goal.time_bound}
            />
            <div class="mt-3">
              <button class="btn btn-primary">Keep Time-Bound Suggestion</button>
            </div>
          </figcaption>
        </figure>
      </div>
    </div>
    <div class="card">
      <figure>
        <figcaption class="p-4 card-body">
          <div class="mt-4 pd-4 flex flex-col items-center">
            {#if goal.days_of_week}
              <span class="block text-xl font-bold mb-2"
                >Select the Days Your SMART Goal Repeats:</span
              >
              <button class="btn btn-primary mt-4" on:click={toggleAll}>
                {#if selectAll}Deselect All{:else}Select All{/if}
              </button>
              <DaysOfWeekSelector daysOfWeek={goal.days_of_week} />
            {/if}
          </div>
          <div class="card">
            <figure>
              <figcaption class="p-4 card-body">
                <label class="block text-lg font-bold mb-2 mt-4" for="goal-time">
                  Set the alert time for your SMART goals on selected days.
                </label>
                <input
                  class="shadow m-2 appearance-none border rounded w-52 py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
                  id="goal-time"
                  type="time"
                  bind:value={goal.time_of_day}
                />
              </figcaption>
            </figure>
          </div>
          <div class="card">
            <figure>
              <figcaption class="p-4 card-body">
                <label class="block text-lg font-bold mb-2" for="goal-date">
                  Choose the Date for Completing Your SMART Goal.
                </label>
                <input
                  class="shadow w-52 appearance-none border rounded py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
                  id="goal-date"
                  type="date"
                  bind:value={goal.date_for_achievement}
                />
              </figcaption>
            </figure>
          </div>
          <div class="card">
            <figure>
              <figcaption class="p-4 card-body">
                <div class="mt-4 flex flex-col items-center">
                  <button class="btn btn-primary" on:click={handleSave}>Save Smart Goal</button>
                </div>
              </figcaption>
            </figure>
          </div>
        </figcaption>
      </figure>
    </div>
  </div>
</div>
