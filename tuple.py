lst = ['loyality program', 'client promotion', 'market research']
lst.append('public relations')
print(lst[2])
lst.insert(1, 'investor relations')
emailMarketing = lst.copy()
emailMarketing.sort()
internalEmails = ['internal communication']
emailMarketing.extend(internalEmails)
print(tuple(emailMarketing))