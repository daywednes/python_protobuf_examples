# import todolist_pb2 as TodoList
import ai_response_pb2 as AIResponse

res = AIResponse.RapidApiResponse()
name = AIResponse.Task.Name(1)
res.task = AIResponse.Task.Value(name)

print(res)


# my_list = TodoList.TodoList()
# my_list.owner_id = 1234
# my_list.owner_name = "Tim"
#
# first_item = my_list.todos.add()
# first_item.state = TodoList.TaskState.Value("TASK_DONE")
# first_item.task = "Test ProtoBuf for Python"
# first_item.due_date = "31.10.2019"
#
#
# # ...
#
# with open("./serializedFile", "wb") as fd:
#     fd.write(my_list.SerializeToString())
# print(my_list.SerializeToString())
#
#
# my_list = TodoList.TodoList()
# with open("./serializedFile", "rb") as fd:
#     my_list.ParseFromString(fd.read())
#
# print(my_list)
