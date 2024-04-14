const team = {
  _players: [
    {
      firstName: 'Pablo',
      lastName: 'Sanchez',
      age: 38
    },
    {
      firstName: 'Baichung', 
      lastName: 'Bhutia', 
      age: 44
    },
    {
      firstName: 'Viswanathan',
      lastNmae: 'Anand',
      age: 51
    }
  ],
  _games: [
    {
      opponent: 'Broncos',
      teamPoints: 42,
      opponentPoints: 27
    },
    {
      opponent: 'Giants',
      teamPoints: 42,
      opponentPoints: 27
    },
    {
      opponent: 'Gods',
      teamPoints: 42,
      opponentPoints: 27
    }
  ],
  get players () {
    return this._players;
  },
  get games () {
    return this._games;
  },
  addPlayer (firstName, lastName, age) {
    const player = {
      firstName,
      lastName,
      age
    };
    this._players.push(player);
  },
  addGame (opponent, teamPoints, opponentPoints) {
    const game = {
      opponent,
      teamPoints,
      opponentPoints
    };
    this._games.push(game)
  }
}

team.addPlayer('Steph', 'Curry', 28);
team.addPlayer('Lisa', 'Leslie', 44);
team.addPlayer('Bugs', 'Bunny', 76);

console.log(team.players);

team.addGame('Titans', 100, 98);
team.addGame('Kami', 100, 98);
team.addGame('Shen', 100, 98);

console.log(team.games);
