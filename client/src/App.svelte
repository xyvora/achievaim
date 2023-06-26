<script>
  import { onMount } from 'svelte';
  import GoalForm from './components/GoalForm.svelte';
  import GoalList from './components/GoalList.svelte';
</script>

<main class="flex flex-col items-center justify-center h-screen bg-gray-100 font-roboto">
  <h1 class="text-3xl font-bold mb-4">SMART Goal Tracker</h1>
  <GoalForm />
  <GoalList />
</main>

<style>
  @import url('https://cdn.jsdelivr.net/npm/tailwindcss@2.2.16/dist/tailwind.min.css');
</style>
