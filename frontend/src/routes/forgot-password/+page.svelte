<script lang="ts">
    let email = '';
    let securityAnswer = '';
    
    function handleSubmit() {
      // handle form submission
      console.log('Email: ', email);
      console.log('Answer to the security question: ', securityAnswer);
    }
  </script>
  
  <div class="page-fade-in flex items-center justify-center min-h-screen">
      <form
        on:submit|preventDefault={handleSubmit}
        class="container shadow-lg rounded-xl mb-8 mx-4 px-4 pt-5 sm:mx-auto sm:px-8 md:max-w-xl lg:max-w-3xl z-10"
      >
        <figure>
          <figcaption class="p-4 card-body flex flex-col space-y-8">
            <h1 class="mb-3 text-xl leading-tight tracking-tight">Forgot your password?</h1>
            <p>Enter your email and the answer to your security question below</p>
            <div class="flex flex-wrap -mx-3 mb-8">
              <div class="w-full px-3 mb-6 sm:mb-8">
                <label for="email" class="block uppercase tracking-wide text-xs font-bold mb-3">Your email</label>
                <input type="email" name="email" id="email" placeholder="name@company.com" class="appearance-none block w-full bg-grey-lighter text-grey-darker border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" required>
              </div>
              <div class="w-full px-3 mb-6 sm:mb-8">
                <label for="security-answer" class="block uppercase tracking-wide text-xs font-bold mb-3">If you could have any superpower, what would it be?</label>
                <input type="text" name="security-answer" id="security-answer" placeholder="Flying" class="appearance-none block w-full bg-grey-lighter text-grey-darker border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" required>
              </div>
            </div>
            <div class="flex items-center justify-between mb-8">
              <button type="submit" class="btn btn-primary" id="btn-reset">Reset password</button>
            </div>
          </figcaption>
        </figure>
      </form>
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
    
      .page-fade-in {
        animation: fadeIn 1s ease-in-out;
      }
    </style>
  