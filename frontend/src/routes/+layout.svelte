<script lang="ts">
  import '../app.css';
  import Navbar from '$lib/components/Navbar.svelte';
</script>

<div class="flex flex-col h-screen">
  <Navbar />
  <slot />
</div>

<style>
  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }

  :global(.page-fade-in) {
    animation: fadeIn 1s ease-in-out;
  }
</style>
