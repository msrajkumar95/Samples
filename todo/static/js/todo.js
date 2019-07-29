var app = angular.module('toDo',[]);
app.controller('toDoController', function($scope, $http) {
	$http.get('/api/todo').then(function(response) {
		$scope.todoList = response.data;
	});
	$scope.add = function() {
		var data = {task: $scope.todoInput};
		$http.post('/api/todo', data).then(function(response) {
			$scope.todoList.push(response.data);
		});
		$scope.todoInput = '';
	};
	$scope.delete = function() {
		var oldList = $scope.todoList;
		$scope.todoList = [];
		angular.forEach(oldList, function(todo) {
			if (todo.done) {
				$http.delete('/api/todo' + todo.id)
			}
			else {
				$scope.todoList.push(todo);
			}
		})
	};
	$scope.update = function() {
		var data = {task: $scope.todoInput};
		angular.forEach($scope.todoList, function(todo, index) {
			if (todo.done) {
				$http.put('/api//todo' + todo.id, data).then(function(response) {
					$scope.todoList[index] = response.data;
				});
				$scope.todoInput = '';
			}
		})
	};
});
