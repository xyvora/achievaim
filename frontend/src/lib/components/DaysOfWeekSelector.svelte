<script lang="ts">
  import type { DaysOfWeek } from '$lib/generated';
  import { toTitleCase } from '$lib/utils';

  export let daysOfWeek: DaysOfWeek;
  export let readOnly: boolean = false;
</script>

<div class="grid grid-cols-2 md:grid-cols- gap-5 mt-4">
  {#each Object.entries(daysOfWeek) as [day, value]}
    <div class="rounded shadow p-2">
      <label class="inline-flex items-center">
        {#if !readOnly}
          <input
            type="checkbox"
            class={value ? 'toggle toggle-primary' : 'toggle toggle-info'}
            bind:checked={daysOfWeek}
          />
        {:else}
          <input
            type="checkbox"
            class={value ? 'toggle toggle-primary' : 'toggle toggle-info'}
            checked={value}
            on:click={() => false}
          />
        {/if}
        <span class="ml-2 text-md">{toTitleCase(day)}</span>
      </label>
    </div>
  {/each}
</div>
