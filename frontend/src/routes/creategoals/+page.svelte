
<div class="flex">
    <div class="divider" />
  </div>
  <div class="container mx-auto px-4 pt-5 md:max-w-xl lg:max-w-3xl z-10">
    <div class="mb-5">
      <label class="block text-xl font-bold mb-2" for="goal"> Goal </label>
      <input
        class="shadow appearance-none border rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
        id="goal"
        type="text"
        placeholder="What's your SMART Goal?"
      />
  
      <div class="mt-3 flex flex-col items-left">
        <button
          id="generate"
          class="btn btn-primary"
          on:click={handleClickGenerate}
          disabled={loadingGenerate}
        >
          Generate
        </button>
        {#if loadingGenerate}
          <div class="mt-3 flex justify-center items-center">
            <span class="loading loading-infinity loading-md" />
          </div>
        {/if}
      </div>
      <div class="mt-3 flex flex-col items-right">
        <button
          id="regenerate"
          class="btn btn-primary"
          on:click={handleClickRegenerate}
          disabled={loadingRegenerate}
        >
          Regenerate
        </button>
        {#if loadingRegenerate}
          <div class="mt-3 flex justify-center items-center">
            <span class="loading loading-infinity loading-md" />
          </div>
        {/if}
      </div>
    </div>
  
    <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
      <!-- Specific card -->
      <div class="card bordered">
        <figure>
          <figcaption class="p-4 card-body">
            <h2 class="card-title">Specific</h2>
            <p id="specific" class="text-gray-600" contenteditable="true">
              SmartGoalAI's Specific suggestion
            </p>
            <div class="mt-3">
              <button on:click={regenerate} class="btn btn-primary">Regenerate</button>
            </div>
          </figcaption>
        </figure>
      </div>
  
      <!-- Measurable card -->
      <div class="card bordered">
        <figure>
          <figcaption class="p-4 card-body">
            <h2 class="card-title">Measurable</h2>
            <p id="measurable" class="text-gray-600" contenteditable="true">
              SmartGoalAI's Measurable suggestion
            </p>
            <div class="mt-3">
              <button on:click={regenerate} class="btn btn-primary">Regenerate</button>
            </div>
          </figcaption>
        </figure>
      </div>
  
      <!-- Attainable card -->
      <div class="card bordered">
        <figure>
          <figcaption class="p-4 card-body">
            <h2 class="card-title">Attainable</h2>
            <p id="attainable" class="text-gray-600" contenteditable="true">
              SmartGoalAI's Attainable suggestion
            </p>
            <div class="mt-3">
              <button on:click={regenerate} class="btn btn-primary">Regenerate</button>
            </div>
          </figcaption>
        </figure>
      </div>
  
      <!-- Relevant card -->
      <div class="card bordered">
        <figure>
          <figcaption class="p-4 card-body">
            <h2 class="card-title">Relevant</h2>
            <p id="relevant" class="text-gray-600" contenteditable="true">
              SmartGoalAI's Relevant suggestion
            </p>
            <div class="mt-3">
              <button on:click={regenerate} class="btn btn-primary">Regenerate</button>
            </div>
          </figcaption>
        </figure>
      </div>
  
      <!-- Time-Bound card -->
      <div class="card bordered">
        <figure>
          <figcaption class="p-4 card-body">
            <h2 class="card-title">Time-Bound</h2>
            <p id="time-bound" class="text-gray-600" contenteditable="true">
              SmartGoalAI's Time-Bound suggestion
            </p>
            <div class="mt-3">
              <button on:click={regenerate} class="btn btn-primary">Regenerate</button>
            </div>
          </figcaption>
        </figure>
      </div>
    </div>
  </div>
  
  <div class="mt-4 pd-4 flex flex-col items-center">
    <span class="block text-xl font-bold mb-2">Days of the week</span>
    <button class="btn btn-primary mt-4" on:click={toggleAll}>
      {#if selectAll}Deselect All{:else}Select All{/if}
    </button>
    <div class="grid grid-cols-2 md:grid-cols- gap-5 mt-4">
      {#each daysOfWeek as day (day.name)}
        <div class="rounded shadow p-2">
          <label class="inline-flex items-center">
            <input
              type="checkbox"
              class={day.selected ? 'toggle toggle-primary' : 'toggle toggle-info'}
              bind:checked={day.selected}
            />
            <span class="ml-2 text-md">{day.name}</span>
          </label>
        </div>
      {/each}
    </div>
  </div>
  
  <div class="mt-4 flex flex-col items-center">
    <label class="block text-lg font-bold mb-2" for="goal-date"> Date </label>
    <input
      bind:value={goalDate}
      class="shadow appearance-none border rounded w-1/2 py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
      id="goal-date"
      type="date"
    />
    <label class="block text-lg font-bold mb-2 mt-4" for="goal-time"> Time </label>
    <input
      bind:value={goalTime}
      class="shadow appearance-none border rounded w-1/2 py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
      id="goal-time"
      type="time"
    />
  </div>
  
  <div class="mt-4 flex flex-col items-center">
    <button class="btn btn-primary" on:click={handleClick}>Save Smart Goal</button>
  </div>
  
  <div class="flex">
    <div class="divider" />
  </div>
  
  <footer class="footer items-center p-4 bg-neutral text-neutral-content">
    <div class="items-center grid-flow-col">
      <svg
        width="36"
        height="36"
        viewBox="0 0 24 24"
        xmlns="http://www.w3.org/2000/svg"
        fill-rule="evenodd"
        clip-rule="evenodd"
        class="fill-current"
        ><path
          d="M22.672 15.226l-2.432.811.841 2.515c.33 1.019-.209 2.127-1.23 2.456-1.15.325-2.148-.321-2.463-1.226l-.84-2.518-5.013 1.677.84 2.517c.391 1.203-.434 2.542-1.831 2.542-.88 0-1.601-.564-1.86-1.314l-.842-2.516-2.431.809c-1.135.328-2.145-.317-2.463-1.229-.329-1.018.211-2.127 1.231-2.456l2.432-.809-1.621-4.823-2.432.808c-1.355.384-2.558-.59-2.558-1.839 0-.817.509-1.582 1.327-1.846l2.433-.809-.842-2.515c-.33-1.02.211-2.129 1.232-2.458 1.02-.329 2.13.209 2.461 1.229l.842 2.515 5.011-1.677-.839-2.517c-.403-1.238.484-2.553 1.843-2.553.819 0 1.585.509 1.85 1.326l.841 2.517 2.431-.81c1.02-.33 2.131.211 2.461 1.229.332 1.018-.21 2.126-1.23 2.456l-2.433.809 1.622 4.823 2.433-.809c1.242-.401 2.557.484 2.557 1.838 0 .819-.51 1.583-1.328 1.847m-8.992-6.428l-5.01 1.675 1.619 4.828 5.011-1.674-1.62-4.829z"
        /></svg
      >
      <p>Copyright © 2023 - All right reserved</p>
    </div>
    <div class="grid-flow-col gap-4 md:place-self-center md:justify-self-end">
      <a href={'#'}
        ><svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          class="fill-current"
          ><path
            d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"
          /></svg
        >
      </a>
      <a href={'#'}
        ><svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          class="fill-current"
          ><path
            d="M4.98 3.5c0 1.381-1.11 2.5-2.48 2.5s-2.48-1.119-2.48-2.5c0-1.38 1.11-2.5 2.48-2.5s2.48 1.12 2.48 2.5zm.02 4.5h-5v16h5v-16zm7.982 0h-4.968v16h4.969v-8.399c0-4.67 6.029-5.052 6.029 0v8.399h4.988v-10.131c0-7.88-8.922-7.593-11.018-3.714v-2.155z"
          /></svg
        ></a
      >
    </div>
  </footer>
  