<script>
  import { onMount } from 'svelte';
  import { getGoals, updateGoal } from '../utils/api';

  let goals = [];

  onMount(async () => {
    goals = await getGoals();
  });

  const handleUpdate = async (event, goal) => {
    event.preventDefault();
    await updateGoal(goal);
    goals = await getGoals();
  };
</script>

<ul class="w-1/2">
  {#each goals as goal}
    <li class="px-4 py-2 mb-2 bg-white rounded shadow-md">
      <h3 class="text-lg font-semibold">{goal.name}</h3>

      <form class="mt-4" on:submit="{(e) => handleUpdate(e, goal)}">
        <label class="block mb-2 text-sm font-semibold">Duration:</label>
        <input type="text" class="px-2 py-1 border border-gray-300 rounded" bind:value="{goal.duration}" />

        <label class="block mb-2 text-sm font-semibold">Days of the Week:</label>
        <div class="flex">
          <label class="mr-2">
            <input type="checkbox" bind:checked="{goal.daysOfWeek.monday}" />
            Monday
          </label>
          <label class="mr-2">
            <input type="checkbox" bind:checked="{goal.daysOfWeek.tuesday}" />
            Tuesday
          </label>
          <label class="mr-2">
            <input type="checkbox" bind:checked="{goal.daysOfWeek.wednesday}" />
            Wednesday
          </label>
          <label class="mr-2">
            <input type="checkbox" bind:checked="{goal.daysOfWeek.thursday}" />
            Thursday
          </label>
          <label class="mr-2">
            <input type="checkbox" bind:checked="{goal.daysOfWeek.friday}" />
            Friday
          </label>
          <label class="mr-2">
            <input type="checkbox" bind:checked="{goal.daysOfWeek.saturday}" />
            Saturday
          </label>
          <label class="mr-2">
            <input type="checkbox" bind:checked="{goal.daysOfWeek.sunday}" />
            Sunday
          </label>
        </div>

        <label class="block mb-2 text-sm font-semibold">Repeats Every:</label>
        <input type="text" class="px-2 py-1 border border-gray-300 rounded" bind:value="{goal.repeatsEvery}" />

        <label class="block mb-2 text-sm font-semibold">Progress:</label>
        <div class="flex items-center">
          <input type="range" class="flex-grow h-3 rounded" min="0" max="100" bind:value="{goal.progress}" />
          <span class="ml-2 text-sm">{goal.progress}%</span>
        </div>

        <button type="submit" class="px-4 py-2 mt-4 font-semibold text-white bg-blue-500 rounded hover:bg-blue-600">Update Goal</button>
      </form>
    </li>
  {/each}
</ul>
