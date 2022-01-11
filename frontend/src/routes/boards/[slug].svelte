<script>
	// import Index from '../index.svelte';
	// import { Button } from 'svelte-materialify';

	// let gamePhase = 'choose';
	// let activePlayer = 'A';

	// // what if I create a grid of coordinates
	// let gameCoords = [
	// 	['A1', null],
	// 	['A2', null],
	// 	['A3', null],
	// 	['A4', null],
	// 	['B1', null],
	// 	['B2', null],
	// 	['B3', null],
	// 	['B4', null],
	// 	['C1', null],
	// 	['C2', null],
	// 	['C3', null],
	// 	['C4', null],
	// 	['D1', null],
	// 	['D2', null],
	// 	['D3', null],
	// 	['D4', null]
	// ];

	// // create a list of winning sets???
	// let winningRows = [
	// 	['A1', 'A2', 'A3', 'A4'],
	// 	['B1', 'B2', 'B3', 'B4'],
	// 	['C1', 'C2', 'C3', 'C4'],
	// 	['D1', 'D2', 'D3', 'D4']
	// ];
	// let winningColumns = [
	// 	['A1', 'B1', 'C1', 'D1'],
	// 	['A2', 'B2', 'C2', 'D2'],
	// 	['A3', 'B3', 'C3', 'D3'],
	// 	['A4', 'B4', 'C4', 'D4']
	// ];
	// let winningDiagonals = [
	// 	['A1', 'B2', 'C3', 'D4'],
	// 	['A4', 'B3', 'C2', 'D1']
	// ];
	// let winningSquares = [
	// 	['A1', 'B1', 'A2', 'B2'],
	// 	['A2', 'B2', 'A3', 'B3'],
	// 	['A3', 'B3', 'A4', 'B4'],
	// 	['B1', 'C1', 'B2', 'C2'],
	// 	['B2', 'C2', 'B3', 'C3'],
	// 	['B3', 'C3', 'B4', 'C4'],
	// 	['C1', 'D1', 'C2', 'D2'],
	// 	['C2', 'D2', 'C3', 'D3'],
	// 	['C3', 'D3', 'C4', 'D4'],
	// 	['A1', 'C1', 'A3', 'C3'],
	// 	['A2', 'C2', 'A4', 'C4'],
	// 	['B1', 'D1', 'B3', 'D3'],
	// 	['B2', 'D2', 'B4', 'D4'],
	// 	['A1', 'A4', 'D1', 'D4']
	// ];

	import { session, page } from '$app/stores';
	import { onMount } from 'svelte';

	var error = undefined;
	var isFull = false;
	var players = [];
	var creator = [];
	onMount(async function getBoard() {
		let uid = $page.params.slug;
		const res = await fetch(`http://127.0.0.1:8000/boards/${uid}`, {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json',
				'Content-Type': 'application/x-www-form-urlencoded'
			}
		});
		const body = await res.json();
		console.log(body);
		isFull = body.isFull;
		if (res.status == 200) {
			const board_isFull = body.isFull;
			players = body.players;
			creator = body.creator.name;
			if (board_isFull) {
				isFull = true;
			}
		} else {
			error = `LOS001: ${body.detail}`;
		}
	});
</script>

{#if isFull == false}
	<div class="game">
		<div class="gameboard">
			<div class="boardspot" id="A1" />
			<div class="boardspot" id="A2" />
			<div class="boardspot" id="A3" />
			<div class="boardspot" id="A4" />
			<div class="boardspot" id="B1" />
			<div class="boardspot" id="B2" />
			<div class="boardspot" id="B3" />
			<div class="boardspot" id="B4" />
			<div class="boardspot" id="C1" />
			<div class="boardspot" id="C2" />
			<div class="boardspot" id="C3" />
			<div class="boardspot" id="C4" />
			<div class="boardspot" id="D1" />
			<div class="boardspot" id="D2" />
			<div class="boardspot" id="D3" />
			<div class="boardspot" id="D4" />
		</div>
		<div class="gamepieces">
			<div class="active">
				<div id="activespot" />
			</div>
			<div class="inactive">
				<img class="piece" id="p0001" src="images/p0001.png" />
				<img class="piece" id="p0010" src="images/p0010.png" />
				<img class="piece" id="p0011" src="images/p0011.png" />
				<img class="piece" id="p0100" src="images/p0100.png" />
				<img class="piece" id="p0101" src="images/p0101.png" />
				<img class="piece" id="p0110" src="images/p0110.png" />
				<img class="piece" id="p0111" src="images/p0111.png" />
				<img class="piece" id="p1000" src="images/p1000.png" />
				<img class="piece" id="p1001" src="images/p1001.png" />
				<img class="piece" id="p1010" src="images/p1010.png" />
				<img class="piece" id="p1011" src="images/p1011.png" />
				<img class="piece" id="p1100" src="images/p1100.png" />
				<img class="piece" id="p1101" src="images/p1101.png" />
				<img class="piece" id="p1110" src="images/p1110.png" />
				<img class="piece" id="p1111" src="images/p1111.png" />
			</div>
		</div>
	</div>
{:else}
	<div>Game is Full, Try a different ID</div>
{/if}

<style>
	.game {
		margin: 0 auto;
		width: 90%;
		display: flex;
		flex-flow: row wrap;
		justify-content: center;
		align-items: stretch;
	}

	.banner {
		width: 100%;
		background-color: lightgreen;
		margin-bottom: 1em;
		padding: 0.75em;
		text-align: center;
		font-weight: bold;
		color: black;
	}

	.gameboard {
		box-sizing: content-box;
		width: 280px;
		height: 280px;
		background-color: white;
		margin-right: 25px;
		padding: 1em;
		border: 4px solid orchid;
		border-radius: 1em;
		display: flex;
		flex-flow: row wrap;
	}

	.inactive {
		box-sizing: border-box;
		background-color: white;
		width: 300px;
		padding: 10px;
		display: flex;
		flex-flow: row wrap;
		justify-content: space-around;
		align-items: baseline;
	}

	.piece {
		width: 40px;
		margin: 2px 2px 2px 2px;
	}

	.boardspot {
		width: 25%;
		height: 25%;
		box-sizing: border-box;
		border: 2px solid black;
		display: flex;
		align-items: flex-end;
		justify-content: center;
	}
</style>
