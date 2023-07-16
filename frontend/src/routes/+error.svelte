<script lang="ts">
  import Error from '$lib/components/Error.svelte';
  import { onMount } from 'svelte';

  let loadError = false;

  onMount(async () => {
    setTimeout(() => (loadError = true), 100);
  });
</script>

<svelte:head>
  {#if loadError}
    <title>404 Page not found</title>
  {/if}
</svelte:head>

{#if loadError}
  <Error error={'404 Page not found'} />
{/if}
