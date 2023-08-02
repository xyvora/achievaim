<script lang="ts">
  import type { DaysOfWeek, GoalCreate } from '$lib/generated';
  import DaysOfWeekSelector from '$lib/components/DaysOfWeekSelector.svelte';

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

  const toggleAll = () => {
    selectAll = !selectAll;
    if (goal.days_of_week) {
      Object.keys(goal.days_of_week).forEach((day) => {
        goal.days_of_week![day as keyof DaysOfWeek] = selectAll;
      });
    }
  };
</script>

<div class="mt-3 flex flex-col items-center">
  <div class="card">
    <figure>
      <figcaption class="p-4 card-body flex flex-col items-center">
        {#if goal.days_of_week}
          <div class="flex justify-between items-center w-full">
            <span class="block text-xl font-bold"> Days </span>
            <div class="flex items-center">
              <label class="cursor-pointer label flex items-center">
                <input
                  type="checkbox"
                  class="toggle toggle-primary"
                  bind:checked={selectAll}
                  on:click={toggleAll}
                />
              </label>
              <div class="dropdown dropdown-end">
                <label tabindex="0" class="btn btn-circle btn-ghost btn-xs text-info m-3">
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
                </label>
                <div
                  tabindex="0"
                  class="card compact dropdown-content z-[1] bg-base-100 rounded-box w-64"
                >
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
