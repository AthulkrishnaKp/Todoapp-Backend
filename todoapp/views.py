
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from todoapp.models import Todos
from rest_framework import serializers
from rest_framework import permissions,authentication

class TodoSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Todos
        fields=["task_name","user"]


class TodosView(ModelViewSet):
    serializer_class=TodoSerializer
    queryset=Todos.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[authentication.TokenAuthentication]

    def create(self, request, *args, **kwargs):
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def get_queryset(self):
        return Todos.objects.filter(user=self.request.user)        
    