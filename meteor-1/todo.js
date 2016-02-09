if (Meteor.isClient) {

    Session.setDefault('counter', 0);

    Template.CounterTmpl.helpers({
        counter: function () {
            return Session.get('counter');
        },

        counterIncrement: function(){
            return 3;
        }
    });

    Template.CounterTmpl.events({
        'click button': function () {
            var increment = parseInt($("#CounterIncrement").val());
            Session.set('counter', Session.get('counter') + increment);
        }
    });
}

if (Meteor.isServer) {
    Meteor.startup(function () {
        // code to run on server at startup
    });
}
