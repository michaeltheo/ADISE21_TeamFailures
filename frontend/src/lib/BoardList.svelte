<script>
	import { goto } from '$app/navigation';
	import { Button } from 'svelte-materialify';
	import { session } from '$app/stores';

	let creator_id = $session.user.id;
	let players = [$session.user.name];
	let input_value = '';
	var error = undefined;
	async function createBoard() {
		const res = await fetch('http://127.0.0.1:8000/boards/', {
			method: 'POST',
			body: JSON.stringify({
				creator_id,
				players
			}),
			headers: {
				'Content-Type': 'application/json'
				// 'Content-Type': 'application/x-www-form-urlencoded'
			}
		});
		const body = await res.json();
		console.log($session.user);
		if (res.status == 200) {
			const board_id = body.id;
			goto('/boards/' + board_id);
		} else {
			error = `LOS001: ${body.message}`;
		}
	}
	async function joinBoard() {
		if (input_value.length == 0) {
			const res = await fetch('http://127.0.0.1:8000/boards/random', {
				method: 'GET',
				headers: {
					'Content-Type': 'application/json',
					'Content-Type': 'application/x-www-form-urlencoded'
				}
			});
			const body = await res.json();
			console.log(body);
			if (res.status == 200) {
				const board_id = body.id;
				goto('/boards/' + board_id);
			} else {
				error = `LOS001: ${body.detail}`;
			}
		} else {
			goto('boards/' + input_value);
		}
		input_value = '';
	}
</script>

<div class="d-flex justify-center mt-4 mb-4 flex-column align-center">
	<input placeholder="Enter board ID" bind:value={input_value} />
	<Button rounded on:click={joinBoard} disabled={input_value.length == 0}>Join Board</Button>
	<span class="divider">--------- OR ---------</span>
	<Button rounded on:click={joinBoard}>Join Random Board</Button>
	<span class="divider">--------- OR ---------</span>
	<Button rounded on:click={createBoard}>Create Board</Button>
	{#if error}
		{error}
	{/if}
</div>

<style>
	.divider {
		margin: 1rem 0;
	}
	input {
		border-style: solid;
		border-radius: 25px;
	}
</style>
