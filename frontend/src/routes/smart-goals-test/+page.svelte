<script lang="ts">
  import type { Goals } from '$lib/types';
  import { goto } from '$app/navigation';

  let goals: Goals = {
    active: [
      {
        name: 'Active Placeholder',
        details: 'S.M.A.R.T details here',
        date: new Date('2024-01-01T10:00:00'),
        days: [10],
        editing: false
      }
    ],
    completed: [
      {
        name: 'Completed Placeholder',
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

<div class="container mx-auto p-4">
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
    {#each Object.entries(goals) as [category, value]}
      <div class="bg-white rounded shadow overflow-hidden">
        <div class="bg-gray-200 text-gray-700 text-lg sm:text-xl font-semibold p-3">
          {capitalizeFirstLetter(category)}
        </div>
        <div class="p-4">
          {#if value.length === 0}
            <div
              class="bg-gray-100 border-2 border-dashed border-gray-200 rounded-lg h-40 flex items-center justify-center text-gray-500"
            >
              Add a Goal
            </div>
          {:else}
            {#each value as goal (goal.name)}
              <div
                class={`rounded-lg p-4 sm:p-6 mb-4 ${
                  goal.placeholder ? 'bg-gray-200' : 'bg-white'
                } shadow-sm border border-gray-200 space-y-2 sm:space-y-4`}
              >
                <button
                  class="text-neutral font-bold text-lg sm:text-xl mb-2 cursor-pointer"
                  on:click={() => goto(`/creategoals/${goal.name}`)}
                >
                  {goal.name}
                </button>
                <div class="text-sm sm:text-base text-gray-900 font-bold my-2">Details:</div>
                <p class="text-gray-900"><strong>S:</strong> {goal.specific}</p>
                <p class="text-gray-900"><strong>M:</strong> {goal.measurable}</p>
                <p class="text-gray-900"><strong>A:</strong> {goal.attainable}</p>
                <p class="text-gray-900"><strong>R:</strong> {goal.relevant}</p>
                <p class="text-gray-900"><strong>T:</strong> {goal.timeBound}</p>
                <div class="grid grid-cols-2 gap-2 text-xs sm:text-sm text-gray-500 mt-4">
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
          {/if}
        </div>
      </div>
    {/each}
  </div>
</div>
