from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from .models import Todo
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def home(request):
    if request.method == 'GET':
        return Response({
            'status': '200',
            'message': 'Yes! Django REST Framework is working!!!',
            'method_called': 'You called GET method',
        })
    elif request.method == 'POST':
        return Response({
            'status': '200',
            'message': 'Yes! Django REST Framework is working!!!',
            'method_called': 'You called POST method',
        })
    elif request.method == 'PUT':
        return Response({
            'status': '200',
            'message': 'Yes! Django REST Framework is working!!!',
            'method_called': 'You called PUT method',
        })
    elif request.method == 'PATCH':
        return Response({
            'status': '200',
            'message': 'Yes! Django REST Framework is working!!!',
            'method_called': 'You called PATCH method',
        })
    elif request.method == 'DELETE':
        return Response({
            'status': '200',
            'message': 'Yes! Django REST Framework is working!!!',
            'method_called': 'You called DELETE method',
        })
    else:
        return Response({
            'status': '400',
            'message': 'Yes! Django REST Framework is working!!!',
            'method_called': 'You called invalid method',
        })

@api_view(['GET'])
def get_todo(request):
    todo_objs = Todo.objects.all()
    serializer = TodoSerializer(todo_objs, many=True)

    return Response({
        'status': 'True',
        'message': 'Todo fetched successfully',
        'data': serializer.data,
    })



@api_view(['POST'])
def post_todo(request):
    try:
        data=request.data
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'True',
                'message': 'Success Data',
                'data': serializer.data,
            })

        return Response({
            'status': 'False',
            'message': 'Invalid Data',
            'data': serializer.errors,
        })
    except Exception as e:
        print(e)
    return Response({
        'status': 'False',
        'message': 'Failed to create todo',
    })


@api_view(['PATCH'])
def patch_todo(request):
    try:
        data = request.data
        if not data.get('uid'):
            return Response({
                'status': False,
                'message': 'uid is required',
                'data': {}
            })
        obj = Todo.objects.get(uid=data.get('uid'))
        serializer = TodoSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'success data',
                'data': serializer.data
            })

        return Response({
            'status': 'False',
            'message': 'Invalid Data',
            'data': serializer.errors,
        })
    except Exception as e:
        print(e)
    return Response({
        'status': False,
        'message': 'Invalid Uid',
        'data': {}
    })

@api_view(['PUT'])
def put_todo(request):
    try:
        data = request.data
        if not data.get('uid'):
            return Response({
                'status': False,
                'message': 'uid is required',
                'data': {}
            })
        obj = Todo.objects.get(uid=data.get('uid'))
        serializer = TodoSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'success data',
                'data': serializer.data
            })

        return Response({
            'status': 'False',
            'message': 'Invalid Data',
            'data': serializer.errors,
        })
    except Exception as e:
        print(e)
    return Response({
        'status': False,
        'message': 'Invalid Uid',
        'data': {}
    })

@api_view(['DELETE'])
def delete_todo(request):
    try:
        data = request.data
        if not data.get('uid'):
            return Response({
                'status': False,
                'message': 'uid is required',
                'data': {}
            })
        obj = Todo.objects.get(uid=data.get('uid'))
        obj.delete()
        return Response({
            'status': True,
            'message': 'success data',
            'data': {}
        })
    except Exception as e:
        print(e)
    return Response({
        'status': False,
        'message': 'Invalid Uid',
        'data': {}
    })




# Class Based APIView
class TodoView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # return Response({
        #     'status': '200',
        #     'message': 'Yes! Django REST Framework is working!!!',
        #     'method_called': 'You called GET method',
        # })
        # print(request.user)
        todo_objs = Todo.objects.filter(user=request.user)
        serializer = TodoSerializer(todo_objs, many=True)

        return Response({
            'status': 'True',
            'message': 'Todo fetched successfully',
            'data': serializer.data,
        })

    def post(self, request):
        # return Response({
        #     'status': '200',
        #     'message': 'Yes! Django REST Framework is working!!!',
        #     'method_called': 'You called POST method',
        # })
        try:
            data = request.data
            data['user'] = request.user.id
            serializer = TodoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 'True',
                    'message': 'Success Data',
                    'data': serializer.data,
                })

            return Response({
                'status': 'False',
                'message': 'Invalid Data',
                'data': serializer.errors,
            })
        except Exception as e:
            print(e)
        return Response({
            'status': 'False',
            'message': 'Failed to create todo',
        })

    def put(self, request):
        # return Response({
        #     'status': '200',
        #     'message': 'Yes! Django REST Framework is working!!!',
        #     'method_called': 'You called PUT method',
        # })
        try:
            data = request.data
            if not data.get('uid'):
                return Response({
                    'status': False,
                    'message': 'uid is required',
                    'data': {}
                })
            obj = Todo.objects.get(uid=data.get('uid'))
            serializer = TodoSerializer(obj, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': 'success data',
                    'data': serializer.data
                })

            return Response({
                'status': 'False',
                'message': 'Invalid Data',
                'data': serializer.errors,
            })
        except Exception as e:
            print(e)
        return Response({
            'status': False,
            'message': 'Invalid Uid',
            'data': {}
        })

    def patch(self, request):
        # return Response({
        #     'status': '200',
        #     'message': 'Yes! Django REST Framework is working!!!',
        #     'method_called': 'You called PATCH method',
        # })
        try:
            data = request.data
            if not data.get('uid'):
                return Response({
                    'status': False,
                    'message': 'uid is required',
                    'data': {}
                })
            obj = Todo.objects.get(uid=data.get('uid'))
            serializer = TodoSerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': 'success data',
                    'data': serializer.data
                })

            return Response({
                'status': 'False',
                'message': 'Invalid Data',
                'data': serializer.errors,
            })
        except Exception as e:
            print(e)
        return Response({
            'status': False,
            'message': 'Invalid Uid',
            'data': {}
        })

    def delete(self, request):
        return Response({
            'status': '200',
            'message': 'Yes! Django REST Framework is working!!!',
            'method_called': 'You called DELETE method',
        })


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(detail=False, methods=['GET'])
    def get_timing_todo(self, request):
        objs = TimingsTodo.objects.all()
        serializer = TimingTodoSerializer(objs, many=True)
        return Response({
            'status': 'True',
            'message': 'Todo fetched successfully',
            'data': serializer.data
            })


    @action(detail=False, methods=['post'])
    def add_date_to_todo(self, request):
        try:
            data = request.data
            serializer = TimingTodoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 'True',
                    'message': 'Success Data',
                    'data': serializer.data,
                })
            return Response({
                'status': 'False',
                'message': 'Invalid Data',
                'data': serializer.errors,
                })
        except Exception as e:
            print(e)
            return Response({
                'status': 'False',
                'message': 'Failed to create todo',
                })
