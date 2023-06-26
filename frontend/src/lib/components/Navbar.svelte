<script lang="ts">
  import { page } from '$app/stores';
  import ThemeSelector from './ThemeSelector.svelte';
</script>

<div class="navbar mb-2 shadow-lg bg-neutral text-neutral-content max-h-16">
  <div class="flex-none sm:px-2 sm:mx-2">
    <a href="/">
      Home
      <!-- <img
        src="../../navbar_logo.png"
        alt="logo"
        class="w-48"
      /> -->
    </a>
  </div>
  <div class="flex-1 px-2 mx-2" />
  <div class="flex-none">
    <ul class="menu menu-horizontal px-1">
      <li>
        <a href="create-goals" class:active={$page.url.pathname === '/create-goals'}>Create Goals</a
        >
      </li>
    </ul>
    <ThemeSelector />
  </div>
</div>
