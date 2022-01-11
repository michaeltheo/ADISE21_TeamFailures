<script context="module">
	export async function load({ session }) {
		if (session.user) {
			return {
				status: 302,
				redirect: '/'
			};
		}
		return {};
	}
</script>

<script>
	import LayoutGrid, { Cell } from '@smui/layout-grid';
	import Button from '@smui/button';
	import Textfield from '@smui/textfield';
	import { session } from '$app/stores';
	import { goto } from '$app/navigation';
	// Variables bound to respective inputs via bind:value
	let email = '';
	let password = '';
	let error = '';
	// let notice
	const login = async () => {
		// Reset error from previous failed attempts
		error = undefined;
		// POST method to src/routes/auth/login.js endpoint
		try {
			const res = await fetch('/login', {
				method: 'POST',
				body: JSON.stringify({
					email,
					password
				}),
				headers: {
					'Content-Type': 'application/json'
				}
			});
			if (res.ok) {
				const data = await res.json();
				$session.user = data.user;
				goto('/');
			} else {
				const data = await res.json();
				// console.log(data)
				error = `LOS001: ${data.message}`;
			}
		} catch (err) {
			console.log(err);
			error = 'LOS002: Pleas try it again.';
		}
	};
</script>

<section>
	<LayoutGrid align="middle" style="text-align: center; ">
		<Cell style=" border: 1px solid var(--mdc-theme-secondary, #333); border-radius:10px;">
			<form style="" on:submit|preventDefault={login}>
				<div class="heading">
					<h2>Login</h2>
				</div>

				<Cell span={6} style="margin-bottom:20px;">
					<Textfield
						style="min-width: 250px;"
						required
						variant="outlined"
						bind:value={email}
						label="Email"
						type="Email"
					/>
				</Cell>

				<Cell span={6}>
					<Textfield
						variant="outlined"
						label="Password"
						style="min-width: 250px;"
						type="password"
						required
						name="password"
						bind:value={password}
					/>
				</Cell>

				{#if error}
					<p>{error}</p>
				{/if}
				<div class="buttons-container">
					<Cell span={6}>
						<Button variant="raised" style="width: 250px; " color="primary" type="submit">
							Login
						</Button>
					</Cell>
					<div style="color:gray; margin-top:10px;">Dont have an account?</div>
					<Button class="forgot" href="/register">Register</Button>
				</div>
			</form>
		</Cell>

		<Cell />
	</LayoutGrid>
</section>

<svelte:head>
	<title>Login</title>
</svelte:head>

<style>
	.heading {
		display: flex;
		align-items: center;
		margin-bottom: 10px;
	}
	h2 {
		width: 100%;
		text-align: center;
		margin-right: 24px;
	}
	.back {
		color: brown;
		font-size: 24px;
		height: 24px;
	}
	.back:hover {
		color: blueviolet;
	}
	.forgot {
		color: red;
		text-decoration: none;
		margin: 20px 0;
	}
	.buttons-container {
		text-align: center;
		margin-bottom: 20px;
		margin-top: 20px;
	}
</style>
