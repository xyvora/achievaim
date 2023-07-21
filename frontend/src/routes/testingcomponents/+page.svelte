<script lang="ts">
  import type { Goal, Goals } from '$lib/types';
  import { goto } from '$app/navigation';

  let goals: Goals = {
    active: [
      {
        name: 'Goal 2',
        details: 'S.M.A.R.T details here',
        date: new Date('2024-01-02T14:00:00'),
        days: [15],
        editing: false
      }
    ],
    completed: [
      {
        name: 'Goal 3',
        details: 'S.M.A.R.T details here',
        date: new Date('2024-01-03T16:00:00'),
        days: [20],
        editing: false
      }
    ]
  };

  let showModal = true;
  let selectedGoal: Goal | null = null;

  function saveChanges(goal: Goal, newDetails: string) {
    goal.details = newDetails;
    goal.editing = false;
  }

  function deleteGoal(category: string | null, goal: Goal | null) {
    if (category === null || goal === null) {
      throw new Error('category and goal are required');
    }

    if (category !== 'active' && category !== 'completed') {
      throw new Error('Unknown category');
    }

    const index = goals[category].indexOf(goal);
    goals[category].splice(index, 1);

    showModal = false;
  }
</script>

<div class="flex flex-col justify-center items-center h-screen mx-auto px-4 sm:px-6 lg:px-8">
  <div class="flex flex-wrap justify-center -mx-2 overflow-hidden sm:-mx-3 md:-mx-3 lg:-mx-4 xl:-mx-4">
    {#each Object.entries(goals) as [category, value]}
      <div
        class="my-2 px-2 w-full overflow-hidden sm:my-2 sm:px-2 sm:w-1/2 md:my-3 md:px-3 md:w-1/2 lg:my-4 lg:px-4 lg:w-1/2 xl:my-4 xl:px-4 xl:w-1/2"
      >
        <div class="text-lg font-bold mb-4">{category}</div>
        {#each value as goal (goal.name)}
          <div class="rounded-lg p-6 mb-4 bg-white shadow-sm border border-gray-200">
            <button
              class="text-neutral font-bold text-xl mb-2 cursor-pointer"
              on:click={() => goto('/creategoals')}
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

{#if showModal && selectedGoal}
  <!-- modal code -->
{/if}
