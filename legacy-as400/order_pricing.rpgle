      *
     C     ITEMTYPE      IFEQ      'A'
     C                   EVAL      DISCOUNT = 0.15
     C                   ELSE
     C     CUSTTIER      IFEQ      'G'
     C                   EVAL      DISCOUNT = 0.10
     C                   ELSE
     C                   EVAL      DISCOUNT = 0.05
     C                   ENDIF
     C                   ENDIF
      *
     C                   EVAL      DISCAMT = GROSSAMT * DISCOUNT
     C                   EVAL      NETAMT  = GROSSAMT - DISCAMT
     C                   RETURN
