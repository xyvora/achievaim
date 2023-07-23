<script lang="ts">
  import '../app.css';
  import Navbar from '$lib/components/Navbar.svelte';
  import { isLoading } from '$lib/stores/stores';
  import { onMount } from 'svelte';

  isLoading.set(true);

  onMount(async () => {
    isLoading.set(false);
  });
</script>

<div class="flex flex-col h-screen">
  {#if $isLoading}
    <div class="flex flex-col items-center justify-center h-screen">
      <span class="loading loading-spinner loading-lg text-primary" />
    </div>
  {:else}
    <Navbar />
    <slot />
  {/if}
</div>
