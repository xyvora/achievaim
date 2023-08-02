<script lang="ts">
    import type { GoalCreate } from '$lib/generated';
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
  
    let goalError = false;
  
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
  </div>
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
            <label class="cursor-pointer label flex items-center md:ml-2 mt-2 md:mt-0 w-full md:w-auto justify-end">
              <input type="checkbox" class="toggle toggle-primary" checked />
              <div class="dropdown dropdown-end">
                <label tabindex="0" class="btn btn-circle btn-ghost btn-xs text-info m-3">
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
            <label class="cursor-pointer label flex items-center md:ml-2 mt-2 md:mt-0 w-full md:w-auto justify-end">
              <input type="checkbox" class="toggle toggle-primary" checked />
              <div class="dropdown dropdown-end">
                <label tabindex="0" class="btn btn-circle btn-ghost btn-xs text-info m-3">
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
            <label class="cursor-pointer label flex items-center md:ml-2 mt-2 md:mt-0 w-full md:w-auto justify-end">
              <input type="checkbox" class="toggle toggle-primary" checked />
              <div class="dropdown dropdown-end">
                <label tabindex="0" class="btn btn-circle btn-ghost btn-xs text-info m-3">
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
            <label class="cursor-pointer label flex items-center md:ml-2 mt-2 md:mt-0 w-full md:w-auto justify-end">
              <input type="checkbox" class="toggle toggle-primary" checked />
              <div class="dropdown dropdown-end">
                <label tabindex="0" class="btn btn-circle btn-ghost btn-xs text-info m-3">
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
            <label class="cursor-pointer label flex items-center md:ml-2 mt-2 md:mt-0 w-full md:w-auto justify-end">
              <input type="checkbox" class="toggle toggle-primary" checked />
              <div class="dropdown dropdown-end">
                <label tabindex="0" class="btn btn-circle btn-ghost btn-xs text-info m-3">
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
            </label>
          </div>
        </figcaption>
      </figure>
    </div>
  </div>