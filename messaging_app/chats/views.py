permission_classes = [IsAuthenticated, IsParticipantOfConversation]
from .filters import MessageFilter

filterset_class = MessageFilter
