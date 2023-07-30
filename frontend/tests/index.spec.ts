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
  await page.locator('#login-button').click();
  await expect(page.locator('#user-name-error')).toBeVisible();
});

test('password is required', async ({ page }) => {
  await page.goto('/');
  await page.locator('#login-button').click();
  await expect(page.locator('#password-error')).toBeVisible();
});
