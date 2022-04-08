sig Client{ creates: set Job, completes: set Job }
sig Admin{ initializes: set Category, modifies: set Job }
sig Category{ holds: set Job }
sig Job{ }

fact AdminCreatesCategory {
	Category in Admin.initializes
}

fact CategoryIsUnique {
	~initializes in Category -> one Admin
}

fact AdminCanModifyJob {
	Job in Admin.modifies
}

fact ClientCreatesJob {
	Job in Client.creates
}

fact ClientCompletesJob {
	Job in Client.completes
}

fact CompletedJobMustBeDifferent {
	all c: Client, j: Job | j in c.creates & c.completes => ~completes in Job -> one Client
}

fact JobIsUnique {
	~creates in Job -> one Client
}

fact JobsAreInCategory {
	Job in Category.holds
}

fact JobUniqueToCategory {
	~holds in Job -> one Category
}


run { } for 20 but exactly 2 Client, 5 Job, 2 Category, 1 Admin
