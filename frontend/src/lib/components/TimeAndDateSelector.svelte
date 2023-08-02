<script lang="ts">
    import type { DaysOfWeek, GoalCreate } from '$lib/generated';
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
  </script>
  
  <div class="card">
    <figure>
      <figcaption class="p-4 card-body flex flex-row items-center">
        <label class="text-left text-lg font-bold mb-2" for="goal-time">Time</label>
        <div class="flex-grow flex items-center">
          <input
            class="shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
            id="goal-time"
            type="time"
            bind:value={goal.time_of_day}
          />
          <div class="dropdown dropdown-end ml-3">
            <label tabindex="0" class="btn btn-circle btn-ghost btn-xs text-info cursor-pointer">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="w-4 h-4 stroke-current">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
            </label>
            <div tabindex="0" class="card compact dropdown-content z-[1] bg-base-100 rounded-box w-64">
              <div class="card-body">
                <h2 class="card-title">You needed more info?</h2>
                <p>Here is a description!</p>
              </div>
            </div>
          </div>
        </div>
      </figcaption>
    </figure>
  </div>
  
  <div class="card">
    <figure>
      <figcaption class="p-4 card-body flex flex-row items-center">
        <label class="text-left text-lg font-bold mb-2" for="goal-date">Date</label>
        <div class="flex-grow flex items-center relative">
          <input
            class="shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
            id="goal-date"
            type="date"
            bind:value={goal.date_for_achievement}
          />
          <div class="dropdown dropdown-end ml-3">
            <label tabindex="0" class="btn btn-circle btn-ghost btn-xs text-info cursor-pointer">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="w-4 h-4 stroke-current">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
            </label>
            <div tabindex="0" class="card compact dropdown-content z-[1] bg-base-100 rounded-box w-64">
              <div class="card-body">
                <h2 class="card-title">You needed more info?</h2>
                <p>Here is a description!</p>
              </div>
            </div>
          </div>
        </div>
      </figcaption>
    </figure>
  </div>
  