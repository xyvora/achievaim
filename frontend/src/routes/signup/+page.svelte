<script>
  import AccountInfoForm from '$lib/components/AccountInfoForm.svelte';
  // Any other scripts go here
</script>
<div class="page-fade-in">
<main>
  <AccountInfoForm />
</main>
<style>
  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }

  .page-fade-in {
    animation: fadeIn 1s ease-in-out;
  }
</style>


</div>