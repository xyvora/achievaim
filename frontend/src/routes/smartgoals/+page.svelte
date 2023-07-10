<script>
  import { onMount } from 'svelte';

  let goals = {
      future: [
          { name: 'Goal 1', details: 'S.M.A.R.T details here', date: '01/01/2024', days: '10', time: '10:00 AM', editing: false }
      ],
      inProgress: [
          { name: 'Goal 2', details: 'S.M.A.R.T details here', date: '01/02/2024', days: '15', time: '02:00 PM', editing: false }
      ],
      completed: [
          { name: 'Goal 3', details: 'S.M.A.R.T details here', date: '01/03/2024', days: '20', time: '04:00 PM', editing: false }
      ]
  }

  let showModal = false;
  let selectedGoal;

  function toggleEditing(goal) {
      goal.editing = !goal.editing;
      showModal = false;
  }

  function saveChanges(goal, newDetails) {
      goal.details = newDetails;
      goal.editing = false;
  }

  function deleteGoal(category, goal) {
      let index = goals[category].indexOf(goal);
      goals[category].splice(index, 1);
      showModal = false;
  }
</script>

<style>
  .animate-fade-in-down {
    animation: fade-in-down 0.3s ease-out both;
  }

  @keyframes fade-in-down {
    0% {
      opacity: 0;
      transform: translate3d(0, -50%, 0);
    }

    100% {
      opacity: 1;
      transform: translate3d(0, 0, 0);
    }
  }
</style>

<div class="container mx-auto px-4 sm:px-6 lg:px-8">
  <div class="flex flex-wrap -mx-2 overflow-hidden sm:-mx-3 md:-mx-3 lg:-mx-4 xl:-mx-4">
    {#each ['future', 'inProgress', 'completed'] as category (category)}
      <div class="my-2 px-2 w-full overflow-hidden sm:my-2 sm:px-2 sm:w-1/2 md:my-3 md:px-3 md:w-1/2 lg:my-4 lg:px-4 lg:w-1/3 xl:my-4 xl:px-4 xl:w-1/3">
        <div class="text-lg font-bold mb-4">{category}</div>
        {#each goals[category] as goal (goal.name)}
          <div class="rounded-lg p-6 mb-4 bg-white shadow-sm border border-gray-200">
            <div class="text-neutral font-bold text-xl mb-2 cursor-pointer" on:click={() => {showModal = true; selectedGoal = goal;}}>{goal.name}</div>
            {#if goal.editing}
              <textarea class="w-full h-16 p-2 mb-2 border rounded" bind:value={goal.details}></textarea>
              <button class="py-1 px-4 border rounded bg-blue-500 text-white" on:click={() => saveChanges(goal, goal.details)}>Save</button>
            {:else}
            <div class="text-base text-gray-900 font-bold my-2">S.M.A.R.T</div>
            <p class="text-gray-900"><strong>Specific:</strong> {goal.specific}</p>
            <p class="text-gray-900"><strong>Measurable:</strong> {goal.measurable}</p>
            <p class="text-gray-900"><strong>Attainable:</strong> {goal.attainable}</p>
            <p class="text-gray-900"><strong>Relevant:</strong> {goal.relevant}</p>
            <p class="text-gray-900"><strong>Time-Bound:</strong> {goal.timeBound}</p>
              <div class="grid grid-cols-2 gap-2 text-sm text-gray-500 mt-4">
                <div><strong>Date:</strong></div> <div>{goal.date}</div>
                <div><strong>Days:</strong></div> 
                <div>
                  <div class="flex flex-row">
                    {#each goal.days.split(',') as day}<span class="mx-1">{day}</span>{/each}
                  </div>
                </div>
                <div><strong>Time:</strong></div> <div>{goal.time}</div>
              </div>
            {/if}
          </div>
        {/each}
      </div>
    {/each}
  </div>
  
  
{#if showModal}
  <div class="fixed z-10 inset-0 overflow-y-auto">
    <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
      <div class="fixed inset-0 transition-opacity ease-out duration-500">
        <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
      </div>
      <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:align-middle sm:max-w-lg sm:w-full animate-fade-in-down">
        <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
          <div class="sm:flex sm:items-start">
            <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
              <h3 class="text-lg leading-6 font-medium text-gray-900" id="modal-title">
                What would you like to do with {selectedGoal.name}?
              </h3>
            </div>
          </div>
        </div>
        <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
          <span class="flex w-full rounded-md shadow-sm sm:ml-3 sm:w-auto">
            <button type="button" class="inline-flex justify-center w-full rounded-md border border-transparent px-4 py-2 bg-green-600 text-base leading-6 font-medium text-white shadow-sm hover:bg-green-500 focus:outline-none focus:border-green-700 focus:shadow-outline-green transition ease-in-out duration-150 sm:text-sm sm:leading-5" on:click={() => toggleEditing(selectedGoal)}>
              Edit
            </button>
          </span>
          <span class="mt-3 flex w-full rounded-md shadow-sm sm:mt-0 sm:w-auto">
            <button type="button" class="inline-flex justify-center w-full rounded-md border border-gray-300 px-4 py-2 bg-white text-base leading-6 font-medium text-gray-700 shadow-sm hover:text-gray-500 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue transition ease-in-out duration-150 sm:text-sm sm:leading-5" on:click={() => showModal = false}>
              Cancel
            </button>
          </span>
          <span class="mt-3 flex w-full rounded-md shadow-sm sm:mt-0 sm:w-auto">
            <button type="button" class="inline-flex justify-center w-full rounded-md border border-transparent px-4 py-2 bg-red-600 text-base leading-6 font-medium text-white shadow-sm hover:bg-red-500 focus:outline-none focus:border-red-700 focus:shadow-outline-red transition ease-in-out duration-150 sm:text-sm sm:leading-5" on:click={() => deleteGoal(selectedCategory, selectedGoal)}>
              Delete
            </button>
          </span>
        </div>
      </div>
    </div>
  </div>
{/if}
</div>
