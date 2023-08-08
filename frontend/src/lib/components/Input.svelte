<script lang="ts">
  import Message from '$lib/components/Message.svelte';

  export let inputId: string;
  export let labelText: string;
  export let placeholder: string;
  export let errorMessage: string | null = null;

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  export let value: any;
  export let isError = false;
  export let isPassword = false;
</script>

<div class="form-control">
  <label class="label label-text" for={inputId}>{labelText}</label>
  {#if isPassword}
    {#if isError}
      <input
        type="password"
        {placeholder}
        id={inputId}
        class="input input-bordered input-error"
        bind:value
      />
    {:else}
      <input type="password" {placeholder} id={inputId} class="input input-bordered" bind:value />
    {/if}
  {:else if isError}
    <input
      type="text"
      {placeholder}
      id={inputId}
      class="input input-bordered input-error"
      bind:value
    />
  {:else}
    <input type="text" {placeholder} id={inputId} class="input input-bordered" bind:value />
  {/if}
  {#if isError && errorMessage !== null}
    <Message messageId="{inputId}-error" message={errorMessage} showMessage={true} isError={true} />
  {/if}
</div>
