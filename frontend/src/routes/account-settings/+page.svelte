<script lang="ts">
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';
  import type { PageData } from './$types';
  import AccountInfoForm from '$lib/components/AccountInfoForm.svelte';

  export let data: PageData;

  onMount(() => {
    if (!data.isAuthenticated) {
      goto('/');
    }
  });
</script>

<main>
  <AccountInfoForm />
</main>
