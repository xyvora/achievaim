<script lang="ts">
  import type { User } from '$lib/types';
  let user: User = {
    username: '',
    avatar: '',
    firstName: '',
    lastName: '',
    country: '',
    gmail: ''
  };
</script>

<form class="w-full max-w-lg mx-auto my-10 p-5 bg-white rounded shadow">
  <div class="flex flex-wrap -mx-3 mb-6">
    <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
      <label
        class="block uppercase tracking-wide text-gray-700 text-lg font-bold mb-2"
        for="first-name"
      >
        First Name*
      </label>
      <input
        class="appearance-none block w-full bg-gray-200 text-gray-700 border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"
        id="first-name"
        type="text"
        placeholder="Jane"
        bind:value={user.firstName}
        required
      />
    </div>
    <div class="w-full md:w-1/2 px-3">
      <label
        class="block uppercase tracking-wide text-gray-700 text-lg font-bold mb-2"
        for="last-name"
      >
        Last Name*
      </label>
      <input
        class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
        id="last-name"
        type="text"
        placeholder="Doe"
        bind:value={user.lastName}
        required
      />
    </div>
  </div>
  <div class="flex flex-wrap -mx-3 mb-6">
    <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
      <label
        class="block uppercase tracking-wide text-gray-700 text-lg font-bold mb-2"
        for="username"
      >
        Username*
      </label>
      <input
        class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
        id="username"
        type="text"
        placeholder="jane.doe"
        bind:value={user.username}
        required
      />
    </div>
    <div class="w-full md:w-1/2 px-3">
      <label class="block uppercase tracking-wide text-gray-700 text-lg font-bold mb-2" for="gmail">
        Gmail Account
      </label>
      <input
        class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
        id="gmail"
        type="email"
        placeholder="jane.doe@gmail.com"
        bind:value={user.gmail}
      />
    </div>
  </div>
  <div class="flex flex-wrap -mx-3 mb-6">
    <div class="w-full px-3">
      <label
        class="block uppercase tracking-wide text-gray-700 text-lg font-bold mb-2"
        for="country"
      >
        Country
      </label>
      <input
        class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
        id="country"
        type="text"
        placeholder="United States"
        bind:value={user.country}
      />
    </div>
  </div>
  <div class="flex flex-wrap -mx-3 mb-6">
    <div class="w-full px-3">
      <label
        class="block uppercase tracking-wide text-gray-700 text-lg font-bold mb-2"
        for="avatar"
      >
        Avatar Photo URL
      </label>
      <input
        class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
        id="avatar"
        type="url"
        placeholder="https://example.com/image.jpg"
        bind:value={user.avatar}
      />
    </div>
  </div>
  <div class="flex items-center justify-between">
    <button
      class="bg-primary hover:bg-secondary text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
      type="submit"
      id="btnSubmit"
    >
      Sign Up
    </button>
  </div>
</form>

<style>
  input:invalid {
    border: 2px solid red;
  }
</style>
