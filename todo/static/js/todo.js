var app = angular.module('toDo',[]);
app.controller('toDoController', function($scope, $http) {
	$http.get('/todo/api/').then(function(response) {
		$scope.todoList = [];
		for (var i = 0; i < response.data.length; i++) {
			var todo = {};
			todo.todoText = response.data[i].task;
			todo.done = response.data[i].done;
			$scope.todoList.push(todo);
		}
		console.log(response.data);
	});
	$scope.todoAdd = function() {
		$scope.todoList.push({todoText: $scope.todoInput, done: false});
		$scope.todoInput = '';
	};
	$scope.remove = function() {
		var oldList = $scope.todoList;
		$scope.todoList = [];
		angular.forEach(oldList, function(x) {
			if (!x.done) $scope.todoList.push(x);
		})
	}
})