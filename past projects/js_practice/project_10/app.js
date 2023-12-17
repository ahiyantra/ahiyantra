const menu = {
  _courses: {
    appetizers: [],
    mains: [],
    desserts: []
  },
  get appetizers () {
    return this._courses.appetizers;
  },
  set appetizers (appetizer) {
    this._courses.appetizers.push(appetizer);
  },
  get mains () {
    return this._courses.mains;
  },
  set mains (main) {
    this._courses.mains.push(main);
  },
  get desserts () {
    return this._courses.desserts;
  },
  set desserts (dessert) {
    this._courses.desserts.push(dessert);
  },
  get courses () {
    return {
      appetizers: this.appetizers,
      mains: this.mains,
      desserts: this.desserts
    }
  },
  addDishToCourse (courseName,dishName,dishPrice) {
    const dish = {
      name: dishName,
      price: dishPrice
    };
    if (courseName==='appetizers') {
      this.appetizers=dish;
    } else if (courseName==='mains') {
      this.mains=dish;
    } else if (courseName==='desserts') {
      this.desserts=dish;
    }
  },
  getRandomDishFromCourse (courseName) {
    const dishes=this._courses[courseName];
    const randomIndex=Math.floor(Math.random()*dishes.length);
    return dishes[randomIndex];
  },
  generateRandomMeal () {
    const appetizer=this.getRandomDishFromCourse('appetizers');
    const main=this.getRandomDishFromCourse('mains');
    const dessert=this.getRandomDishFromCourse('desserts');
    const totalPrice=appetizer.price+main.price+dessert.price;
    return `Your order is ${appetizer.name}, ${main.name} & ${dessert.name}. Your bill is ${totalPrice}.`;
  }
};

menu.addDishToCourse('appetizers', 'Caesar Salad', 4.25);
menu.addDishToCourse('appetizers', 'Caesar Soup', 4.25);
menu.addDishToCourse('appetizers', 'Caesar Noodles', 4.25);
menu.addDishToCourse('mains', 'Caesar Chicken', 4.25);
menu.addDishToCourse('mains', 'Caesar Rice', 4.25);
menu.addDishToCourse('mains', 'Caesar Lamb', 4.25);
menu.addDishToCourse('desserts', 'Caesar Parfait', 4.25);
menu.addDishToCourse('desserts', 'Caesar Crepe', 4.25);
menu.addDishToCourse('desserts', 'Caesar Doughnut', 4.25);

const meal = menu.generateRandomMeal();

console.log(meal);
