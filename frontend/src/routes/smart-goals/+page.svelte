<script lang="ts">
  import type { Goal, Goals } from '$lib/types';
  import { goto } from '$app/navigation';

  let goals: Goals = {
    active: [
      {
        name: 'Goal 1',
        details: 'S.M.A.R.T details here',
        date: new Date('2024-01-01T10:00:00'),
        days: [10],
        editing: false
      }
    ],
    completed: [
      {
        name: 'Goal 2',
        details: 'S.M.A.R.T details here',
        date: new Date('2024-01-02T14:00:00'),
        days: [15],
        editing: false
      }
    ]
  };

  function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
  }
</script>

<div class="flex flex-col items-center justify-center h-screen">
  <div class="flex flex-wrap -mx-2 overflow-hidden sm:-mx-3 md:-mx-3 lg:-mx-4 xl:-mx-4 justify-center">
    {#each Object.entries(goals) as [category, value]}
      <div
        class="my-2 px-2 w-full overflow-hidden sm:my-2 sm:px-2 sm:w-1/2 md:my-3 md:px-3 md:w-1/2 lg:my-4 lg:px-4 lg:w-1/3 xl:my-4 xl:px-4 xl:w-1/3"
      >
        <div class="text-lg font-bold mb-4">{capitalizeFirstLetter(category)}</div>
        {#each value as goal (goal.name)}
          <div class="rounded-lg p-6 mb-4 bg-white shadow-sm border border-gray-200 space-y-4">
            <button
              class="text-neutral font-bold text-xl mb-2 cursor-pointer"
              on:click={() => goto(`/creategoals/${goal.name}`)}
            >
              {goal.name}
            </button>
            <div class="text-base text-gray-900 font-bold my-2">S.M.A.R.T</div>
            <p class="text-gray-900"><strong>Specific:</strong> {goal.specific}</p>
            <p class="text-gray-900"><strong>Measurable:</strong> {goal.measurable}</p>
            <p class="text-gray-900"><strong>Attainable:</strong> {goal.attainable}</p>
            <p class="text-gray-900"><strong>Relevant:</strong> {goal.relevant}</p>
            <p class="text-gray-900"><strong>Time-Bound:</strong> {goal.timeBound}</p>
            <div class="grid grid-cols-2 gap-2 text-sm text-gray-500 mt-4">
              <div><strong>Date:</strong></div>
              <div>{goal.date}</div>
              <div><strong>Days:</strong></div>
              <div>
                <div class="flex flex-row">
                  {#each goal.days as day}<span class="mx-1">{day}</span>{/each}
                </div>
              </div>
              <div><strong>Time:</strong></div>
              <div>{goal.time}</div>
            </div>
          </div>
        {/each}
      </div>
    {/each}
  </div>
</div>

<style>
@keyframes bounce {
  0%, 20%, 50%, 80%, 100% {
    transform: translateY(0);
  }
  40% {
    transform: translateY(-20px);
  }
  60% {
    transform: translateY(-10px);
  }
}

button {
  animation: bounce 1s ease ;
}
</style>