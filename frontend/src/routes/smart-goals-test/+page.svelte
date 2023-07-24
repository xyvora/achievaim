<script lang="ts">
  import type { Goals } from '$lib/types';
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

  function capitalizeFirstLetter(string: string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
  }
</script>

<div class="flex flex-col items-center justify-center h-screen">
  <div class="flex flex-wrap -mx-2 overflow-hidden sm:-mx-3 md:-mx-3 lg:-mx-4 xl:-mx-4 justify-center">
    {#each Object.entries(goals) as [category, value]}
      <div class="my-2 px-2 w-full overflow-hidden sm:my-2 sm:px-2 sm:w-full md:my-3 md:px-3 md:w-full lg:my-4 lg:px-4 lg:w-full xl:my-4 xl:px-4 xl:w-full">
        <div class="text-lg font-bold mb-4">{capitalizeFirstLetter(category)}</div>
        {#each value as goal (goal.name)}
          <div class={`rounded-lg p-6 mb-4 bg-white ${category === 'completed' ? 'bg-gray-200' : ''} shadow-lg border border-gray-200 space-y-4 transition-transform transform hover:scale-105`}>
            <button
              class={`text-neutral font-bold text-xl mb-2 cursor-pointer hover:text-blue-500 transition-colors ${category === 'completed' ? 'text-gray-500' : ''}`}
              on:click={() => goto(`/creategoals/${goal.name}`)}
            >
              {goal.name}
            </button>
            <div class="text-base text-gray-900 font-bold my-2">S.M.A.R.T</div>
            <p class="text-gray-900"><strong>Details:</strong> {goal.details}</p>
            <div class="grid grid-cols-2 gap-2 text-sm text-gray-500 mt-4">
              <div><strong>Date:</strong></div>
              <div>{new Intl.DateTimeFormat('en-US').format(goal.date)}</div>
              <div><strong>Days:</strong></div>
              <div>
                <div class="flex flex-row">
                  {#each goal.days as day}<span class="mx-1">{day}</span>{/each}
                </div>
              </div>
            </div>
            {#if category === 'completed'}
            <div class="flex items-center justify-center h-12 animate-pulse bg-green-200 rounded-full">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-6 h-6 text-green-700">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
              </svg>
            </div>
            {:else}
            <div class="flex items-center justify-center h-12 animate-pulse bg-blue-200 rounded-full">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-6 h-6 text-blue-700">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
              </svg>
            </div>
            {/if}
          </div>
        {/each}
      </div>
    {/each}
  </div>
</div>

<style>
  .hover\:text-blue-500:hover {
    color: #3b82f6;
  }
  
  .transition-colors {
    transition: color 0.2s ease-in-out;
  }

  .transition-transform {
    transition: transform 0.3s ease-in-out;
  }

  .hover\:scale-105:hover {
    transform: scale(1.05);
  }

  @keyframes pulse {
    0%, 100% {
      opacity: 1;
    }
    50% {
      opacity: 0.5;
    }
  }
  
  .animate-pulse {
    animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
  }
</style>
