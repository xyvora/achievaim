<script lang="ts">
  import '../app.css';
  import Navbar from '$lib/components/Navbar.svelte';
</script>

<div class="flex flex-col h-screen">
  <Navbar />
  <slot />
</div>
