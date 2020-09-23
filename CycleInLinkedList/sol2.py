def cycle(head):
   rabbit=head
   tortoise=head
   while(rabbit and rabbit.next):
      rabbit=rabbit.next.next
      tortoise=tortoise.next
      if(tortoise==rabbit):
         return True
   return False


