<script lang="ts">
  import type { DaysOfWeek } from '$lib/generated';
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
    Object.keys(daysOfWeek).forEach((day) => {
      daysOfWeek[day as keyof DaysOfWeek] = selectAll;
    });
  };
</script>

<div class="mt-3 flex flex-col items-center">
  <div class="card">
    <figure>
      <figcaption class="p-4 card-body flex flex-col items-center">
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
                    <button
                      class="card compact dropdown-content z-[1] bg-base-100 rounded-box w-64"
                    >
                      <div class="card-body">
                        <h2 class="card-title">You needed more info?</h2>
                        <p>Here is a description!</p>
                      </div>
                    </button>
                  </button>
                </div>
              </label></label
            >
          </div>
        </div>
        <DaysOfWeekSelector {daysOfWeek} />
      </figcaption>
    </figure>
  </div>
</div>
