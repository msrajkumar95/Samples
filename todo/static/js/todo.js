var app = angular.module('toDo',[]);
app.controller('toDoController', function($scope, $http) {
	$http.get('/todo/api/').then(function(response) {
		$scope.todoList = response.data;
	});
	$scope.add = function() {
		var data = {task: $scope.todoInput};
		$http.put('/todo/api/', data).then(function(response) {
			$scope.todoList.push(response.data);
		});
		$scope.todoInput = '';
	};
	$scope.remove = function() {
		var oldList = $scope.todoList;
		$scope.todoList = [];
		angular.forEach(oldList, function(todo) {
			if (todo.done) {
				$http.delete('/todo/api/' + todo.id + '/')
			}
			else {
				$scope.todoList.push(todo);
			}
		})
	};
});