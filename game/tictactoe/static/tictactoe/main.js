const board = document.getElementById("game-board");
		board.addEventListener("click", (e)=>{
			let data = {
				miniBoard: e.target.dataset.board, 
				cell: e.target.dataset.cell,
				gameId: 2,
				player: true
			}
			fetch('game/', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify(data)
			})
			.then(response => response.json())
			.then(data => {
				renderData(data)
			})
			.catch(error => {
				console.error('Error sending move:', error);
			});
		});

		function renderData(data){
			const cellElement = document.querySelector(
				`.cell[data-board='${data.miniBoard}'][data-cell='${data.cell}']`
        	);
			if(data.moveAllowed){
				console.log("valid move")
				cellElement.textContent = "X"
			}
			else{
				console.log("invalid move")
			}
		}