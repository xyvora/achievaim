import { expect, test } from '@playwright/test';

test('page loads', async ({ page }) => {
  await page.goto('/');
  await expect(page.locator('#navbar')).toBeVisible();
});

test('navbar link is active', async ({ page }) => {
  await page.goto('/');
  await expect(page.getByRole('link', { name: /home/ })).toHaveClass('rounded bg-white');
});

test('user name is required', async ({ page }) => {
  await page.goto('/');
  await expect(page.locator('#user-name')).toBeVisible();
  await page.locator('#login-button').click();
  await expect(page.locator('#user-name-error')).toBeVisible();
});

test('password is required', async ({ page }) => {
  await page.goto('/');
  await expect(page.locator('#password')).toBeVisible();
  await page.locator('#login-button').click();
  await expect(page.locator('#password-error')).toBeVisible();
});

test('signup', async ({ page }) => {
  await page.goto('/');
  await expect(
    page.getByRole('link', { name: 'Are your Goals Smart yet? Sign up here!' })
  ).toBeVisible();
  await page.getByRole('link', { name: 'Are your Goals Smart yet? Sign up here!' }).click();
  await expect(page.locator('#first-name')).toBeVisible();
  await expect(page.locator('#last-name')).toBeVisible();
  await expect(page.locator('#user-name')).toBeVisible();
  await expect(page.locator('#password')).toBeVisible();
  await expect(page.locator('#verify-password')).toBeVisible();
  await expect(page.locator('#btn-sign-up')).toBeVisible();
  await page.locator('#first-name').fill('Imma');
  await page.locator('#last-name').fill('User');
  await page.locator('#user-name').fill('immauser');
  await page.locator('#password').fill('mypassword');
  await page.locator('#verify-password').fill('mypassword');
  await page.locator('#btn-sign-up').click();
  await expect(page.locator('#btn-sign-up')).not.toBeVisible();
  await expect(page.locator('#btn-log-out')).toBeVisible();
  await expect(page.locator('#btn-delete')).toBeVisible();
  page.once('dialog', async (dialog) => {
    await dialog.accept();
  });
  await page.locator('#btn-delete').click();
  await expect(page).toHaveURL('/');
});
