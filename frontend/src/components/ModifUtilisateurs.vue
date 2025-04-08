<template>
  <div class="user-container">
    <h2>Utilisateurs</h2>
		<div class="user-header">
			<table>
				<th>Pseudo</th>
				<th>Niveau actuel</th>
				<th>Points actuels</th>
				<th></th>
				<tr>
					<td>Exemple</td>
					<td>
					<p>Avancé</p>
					<select name="level">
						<option> Niveau actuel </option>
						<option value="debutant">Débutant</option>
						<option value="intermediare">Intermédiaire</option>
						<option value="avance">Avancé</option>
						<option value="expert">Expert</option>
					</select>
					</td>
					<td>
						<p>5</p>
						<select name="point">
						<option> Points actuels </option>
						<option>1</option>
						<option>2</option>
						<option>3</option>
						<option>4</option>
						<option>5</option>
						<option>6</option>
						<option>7</option>
					</select>
					</td>
					<td>
						<button class="delete">Supprimer</button>
					</td>
				</tr>
			</table>
		</div>
  </div>
</template>

<style>
.user-container {
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #f9f9f9;
}


.delete{
	width: 100%;
  padding: 10px;
  background-color: red;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

p {
	text-align: center;
}

.delete:hover{
	background-color: darkred;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

</style>
